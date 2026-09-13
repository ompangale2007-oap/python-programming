def prod(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * prod(n - 1)

n = int(input("Enter n: "))
print(prod(n))