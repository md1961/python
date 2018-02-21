from collections import defaultdict
import re

"""
5  =>  {'num': 5}
x  =>  {'var': 'x'}
(+ x x)  =>  {'arg1': {'var': 'x'}, 'arg0': {'var': 'x'}, 'op': '+'}
(- x x)  =>  {'arg1': {'var': 'x'}, 'arg0': {'var': 'x'}, 'op': '-'}
(* x 2)  =>  {'arg1': {'num': 2}, 'arg0': {'var': 'x'}, 'op': '*'}
(/ x 2)  =>  {'arg1': {'num': 2}, 'arg0': {'var': 'x'}, 'op': '/'}
(^ x 2)  =>  {'arg1': {'num': 2}, 'arg0': {'var': 'x'}, 'op': '^'}
(cos x)  =>  {'arg0': {'var': 'x'}, 'func': 'cos'}
(sin x)  =>  {'arg0': {'var': 'x'}, 'func': 'sin'}
(tan x)  =>  {'arg0': {'var': 'x'}, 'func': 'tan'}
(exp x)  =>  {'arg0': {'var': 'x'}, 'func': 'exp'}
(ln x)  =>  {'arg0': {'var': 'x'}, 'func': 'ln'}
(+ x (+ x x))  =>  {'arg1': {'arg1': {'var': 'x'}, 'arg0': {'var': 'x'}, 'op': '+'}, 'arg0': {'var': 'x'}, 'op': '+'}
(- (+ x x) x)  =>  {'arg1': {'var': 'x'}, 'arg0': {'arg1': {'var': 'x'}, 'arg0': {'var': 'x'}, 'op': '+'}, 'op': '-'}
(* 2 (+ x 2))  =>  {'arg1': {'arg1': {'num': 2}, 'arg0': {'var': 'x'}, 'op': '+'}, 'arg0': {'num': 2}, 'op': '*'}
(/ 2 (+ 1 x))  =>  {'arg1': {'arg1': {'var': 'x'}, 'arg0': {'num': 1}, 'op': '+'}, 'arg0': {'num': 2}, 'op': '/'}
(cos (+ x 1))  =>  {'arg0': {'arg1': {'num': 1}, 'arg0': {'var': 'x'}, 'op': '+'}, 'func': 'cos'}
(sin (+ x 1))  =>  {'arg0': {'arg1': {'num': 1}, 'arg0': {'var': 'x'}, 'op': '+'}, 'func': 'sin'}
(sin (* 2 x))  =>  {'arg0': {'arg1': {'var': 'x'}, 'arg0': {'num': 2}, 'op': '*'}, 'func': 'sin'}
(tan (* 2 x))  =>  {'arg0': {'arg1': {'var': 'x'}, 'arg0': {'num': 2}, 'op': '*'}, 'func': 'tan'}
(exp (* 2 x))  =>  {'arg0': {'arg1': {'var': 'x'}, 'arg0': {'num': 2}, 'op': '*'}, 'func': 'exp'}
(cos (* 2 x))  =>  {'arg0': {'arg1': {'var': 'x'}, 'arg0': {'num': 2}, 'op': '*'}, 'func': 'cos'}
(^ x 3)  =>  {'arg1': {'num': 3}, 'arg0': {'var': 'x'}, 'op': '^'}
"""
def var_and_degree(tree):
    if 'num' in tree:
        return (None, 0)
    if 'var' in tree:
        return ('x', 1)
    if 'op' in tree:
        op = tree['op']
        v0, d0 = var_and_degree(tree['arg0'])
        v1, d1 = var_and_degree(tree['arg1'])
        if op == '^':
            if v1 is not None:
                raise NotImplementedError(str(tree))
            return (v0, d0 * tree['arg1']['num'])
        elif op in ('+', '-'):
            if d1 == 0 or (v0 == v1 and d0 == d1):
                return (v0, d0)
            if d0 == 0:
                return (v1, d1)
            return (None, -1)  # mixed var's or degrees
        else:  # op in ('*', '/')
            if v0 != v1 and d0 > 0 and d1 > 0:
                raise NotImplementedError(str(tree))
            v = v1 if d0 == 0 else v0
            d = d0 + d1 if op == '*' else d0 - d1
            return (v, d)
    else:  # 'func'
        return (tree, 1)


def collapse(trees):
    nums = []
    vars = []
    for tree in trees:
        (nums if 'num' in tree else vars).append(tree)
    while len(nums) > 1:
        num = nums.pop()
        nums[0] = {'num': nums[0]['num'] * num['num']}
    i = 0
    while i < len(nums) - 1:
        j = i + 1
        while j < len(nums):

def degree_of(var_name, tree):
    if tree.get('var') == var_name:
        return 1
    if tree.get('op') == '^' and tree['arg0'].get('var') == var_name:
        num = tree['arg1'].get('num')
        if num is None:
            raise NotImplementedError(str(tree))
        return num
    return 0

def multiply(tree0, tree1):
    multipliers = []
    divisors = []
    for tree in (tree0, tree1):
        if 'num' in tree or 'var' in tree or tree.get('op') == '^':
            multipliers.append(tree)
        elif 'op' in tree:
            multipliers.append(tree['arg0'])
            if tree['op'] = '*':
                multipliers.append(tree['arg1'])
            elif tree['op'] = '/':
                divisors.append(tree['arg1'])
            else:
                raise NotImplementedError("op of '+' or '-'")
    if len(multipliers) == 2 and not divisors:
        d0 = degree_of('x', tree0)
        d1 = degree_of('x', tree1)
        if d0 > 0 and d1 > 0:
            return {'op': '^', 'arg0': {'var': 'x'}, 'arg1': {'num': d0 + d1}}
    multipliers = collpase(multipliers)
    divisors    = collpase(divisors)
    

def arrange(tree):
    if 'num' in tree or 'var' in tree:
        return [tree]
    if 'op' in tree:
        op   = tree['op']
        arg0 = tree['arg0']
        arg1 = tree['arg1']
        trees0 = arrange(arg0)
        trees1 = arrange(arg1)
        if op in ('+', '-'):
            if op == '-':
                trees1 = map(lambda t: {'op': '*', 'arg0': t, 'arg1': -1}, t in trees1)
            return trees0 + trees1
        if op == '*':
            if len(trees0) == 1 and len(trees1) == 1:
                return [multiply(trees0[0], trees1[0])]


def scan_first(pattern, s):
    token = ''
    m = re.match(pattern, s)
    if m:
        token = m.group(0)
        s = re.sub(r'\A' + pattern, '', s).lstrip()
    return (token, s)

def make_tree(s):
    s = s.strip()
    tree = {}
    if s[0] == '(':
        s = s.lstrip('(')
        op, s = s.split(None, 1)
        kind, n_args = ('op', 2) if len(op) == 1 else ('func', 1)
        tree[kind] = op
        for n in range(n_args):
            key = 'arg{}'.format(n)
            tree[key], s = make_tree(s)
    else:
        token, s = scan_first(r'[\w\d]+', s)
        if token:
            if re.match(r'\d+\Z', token):
                tree['num'] = int(token)
            else:
                tree['var'] = token
    s = s.strip().lstrip(')')
    return (tree, s.strip())

def diff(s):
    return make_tree(s)[0]


if __name__ == '__main__':
    args = [
        "5",
        "x",
        "(+ x x)",
        "(- x x)",
        "(* x 2)",
        "(/ x 2)",
        "(^ x 2)",
        "(cos x)",
        "(sin x)",
        "(tan x)",
        "(exp x)",
        "(ln x)",
        "(+ x (+ x x))",
        "(- (+ x x) x)",
        "(* 2 (+ x 2))",
        "(/ 2 (+ 1 x))",
        "(cos (+ x 1))",
        "(sin (+ x 1))",
        "(sin (* 2 x))",
        "(tan (* 2 x))",
        "(exp (* 2 x))",
        "(cos (* 2 x))",
        "(^ x 3)",
    ]
    """
    args = [
        "(+ x 2)",
        "(* 2 (+ x 2))",
    ]
    """
    for s in args:
        print("{}  =>  ".format(s), end='')
        print(diff(s), end='')
        print(" ({})".format(var_and_degree(diff(s))))

    quit()


    import sys
    sys.path.insert(0, './codewars')
    import test

    def testThis(config, n = 1, val=0):
        for msg,expected,inp in config:
            msg,expected,inp = (s.format(val) for s in (msg,expected,inp))
            for _ in range(n-1): inp = diff(inp)
            test.assert_equals(diff(inp), expected, msg)


    test.describe("Sample tests")

    config = [  ("constant should return 0", "0", "5"),
                ("x should return 1", "1", "x"),
                ("x+x should return 2", "2", "(+ x x)"),
                ("x-x should return 0", "0", "(- x x)"),
                ("2*x should return 2", "2", "(* x 2)"),
                ("x/2 should return 0.5", "0.5", "(/ x 2)"),
                ("x^2 should return 2*x", "(* 2 x)", "(^ x 2)"),
                ("cos(x) should return -1 * sin(x)", "(* -1 (sin x))", "(cos x)"),
                ("sin(x) should return cos(x)", "(cos x)", "(sin x)"),
                ("tan(x) should return 1 + tan(x)^2", "(+ 1 (^ (tan x) 2))", "(tan x)"),
                ("exp(x) should return exp(x)", "(exp x)", "(exp x)"),
                ("ln(x) should return 1/x", "(/ 1 x)", "(ln x)")]
                
    testThis(config)
    print("<COMPLETEDIN::>")


    test.describe("Sample tests")

    config = [  ("x+(x+x) should return 3", "3", "(+ x (+ x x))"),
                ("(x+x)-x should return 1", "1", "(- (+ x x) x)"),
                ("2*(x+2) should return 2", "2", "(* 2 (+ x 2))"),
                ("2/(1+x) should return -2/(1+x)^2", "(/ -2 (^ (+ 1 x) 2))", "(/ 2 (+ 1 x))"),
                ("cos(x+1) should return -1 * sin(x+1)", "(* -1 (sin (+ x 1)))", "(cos (+ x 1))"),
                ("sin(x+1) should return cos(x+1)", "(cos (+ x 1))", "(sin (+ x 1))"),
                ("sin(2*x) should return 2*cos(2*x)", "(* 2 (cos (* 2 x)))", "(sin (* 2 x))"),
                ("tan(2*x) should return 2 * (1 + tan(2*x)^2)", "(* 2 (+ 1 (^ (tan (* 2 x)) 2)))", "(tan (* 2 x))"),
                ("exp(2*x) should return 2*exp(2*x)", "(* 2 (exp (* 2 x)))", "(exp (* 2 x))")]

    testThis(config)

    result = diff("(cos (* 2 x))")
    test.expect(result in ("(* 2 (* -1 (sin (* 2 x))))", "(* -2 (sin (* 2 x)))"), "Expected (* 2 (* -1 (sin (* 2 x)))) or (* -2 (sin (* 2 x))) but got " + result)

    print("<COMPLETEDIN::>")


    test.describe("Second derivatives")

    config =  [("Second deriv. sin(x) should return -1 * sin(x)", "(* -1 (sin x))", "(sin x)"),
               ("Second deriv. exp(x) should return exp(x)", "(exp x)", "(exp x)")]

    testThis(config, 2)

    result = diff(diff("(^ x 3)"))
    test.expect(result in ("(* 3 (* 2 x))", "(* 6 x)"), "Expected (* 3 (* 2 x)) or (* 6 x) but got " + result)

