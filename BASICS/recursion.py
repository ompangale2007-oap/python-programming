def sum_(n):
    if n<=0:
        return 0
    return n + sum_(n-1)
a=int(input("Enter n : "))
b=sum_(a)
print(b)
