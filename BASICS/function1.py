def greatest():
    a = float(input("enter a: "))
    b = float(input("enter b: "))
    c = float(input("enter c: "))
    
    if a > b and a > c:
        print("a is greater")
    elif b > a and b > c:
        print("b is greater")
    elif c > a and c > b:
        print("c is greater")
    else:
        print("Two or more numbers are equal")


greatest()