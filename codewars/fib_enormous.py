def fib(n):
    def fib_with_t(a, b, p, q, n):
        if n == 0:
            return a
        if n % 2 == 0:
            """
            a2 = p * (p * a + q * b) + q * (p * b + q * (a + b))
               = ppa + pqb + pqb + qqa + qqb
               = (pp + qq) * a + (2pq + qq) * b
            b2 = p * (p * b + q * (a + b)) + q * ((p * a + q * b) + (p * b + q * (a + b)))
               = ppb + pqa + pqb + pqa + qqb + pqb + qqa + qqb
               = (2pq + qq) * a + (pp + 2pq + 2qq) * b
               = (pp + qq) * b + (2pq + qq) * (a + b)
            """
            p2 = p ** 2 + q ** 2
            q2 = 2 * p * q + q ** 2
            return fib_with_t(a, b, p2, q2, n / 2)
        a2 = p * a + q * b
        b2 = p * b + q * (a + b)
        return fib_with_t(a2, b2, p, q, n - 1)
    
    return fib_with_t(0, 1, 0, 1, n)


if __name__ == '__main__':
    print(fib(1e6))
