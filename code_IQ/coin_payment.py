total = int(input())

def n_payments(total, coins):
    coin = coins[0]
    if len(coins) == 1:
        assert coin == 1, "coin must be 1 (got {})".format(coin)
        return 1
    count = 0
    for n_coins in range(total // coin + 1):
        rest = total - coin * n_coins
        count += n_payments(rest, coins[1::])
    return count

print(n_payments(total, (500, 100, 50, 10, 5, 1)))
