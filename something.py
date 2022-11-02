def outer():
    x = "OUter"

    def inner():
        nonlocal x
        # x = "inner"
        print("from inner function,", x)

    inner()
    print("outer x", x)


outer()
