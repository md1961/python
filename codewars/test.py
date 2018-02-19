def describe(desc):
    print(desc)

def it(exp):
    print(exp)

def assert_equals(actual, expected, msg=""):
    if actual == expected:
        print("OK")
    else:
        msg = ''
        print("NG: ", end='')
        if msg:
            print(msg)
            print("    ", end='')
        print("'{}' expected, got '{}'".format(expected, actual))
