def fun(n):
    if n == 0:
        return 0
    print("Hello World !")
    return fun( n - 1)

fun(5)
