def REMOVE(n):
    L = ["ABC", "DEF", "GHI"]
    if 0 <= n < len(L):
        L.pop(n)
        print(L)
    else:
        print("Invalid index position")
n= int(input("Enter position of word which you want to remove: "))
REMOVE(n)