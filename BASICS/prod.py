def prod(n):
    if n <= 1:
        print(f"Product till 1 is : 1")
        return 1
    else:
        result = n * prod(n - 1)
        print(f"Product till {n} is : {result}")
        return result

n = int(input("Enter n : "))
if n == 0:
    print("0")
else:
    prod(n)