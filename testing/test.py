def assert_equals(a, b, message = ""):
    print("pass: " + str(a) if (a == b) else "fail, expected " + str(b) + " but got " + str(a))