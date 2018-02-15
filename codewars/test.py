def describe(desc):
    print(desc)

def it(exp):
    print(exp)

def assert_equals(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print("NG: '{}' expected, got '{}'".format(expected, actual))
