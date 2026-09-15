Balance=100000;
a=int(input("Enter amount : "))
b=int(input("Enter PIN : "))
if b == 1630:
    print(" ")
    if a<=Balance:
        print("Successfully withdrawl")
        print("Available Balance is : ",Balance-a)
        print("Thank You ")
    else:
         print("insufficient Balance ")
else:
     print("Incorrect PIN ")
