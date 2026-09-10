
def print_square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()  


n = int(input("Enter n: "))
print_square(n)