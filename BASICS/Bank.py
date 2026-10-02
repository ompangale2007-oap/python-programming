Balance = 100000
amount = int(input("Enter amount for withdrawl : "))
if Balance > amount:
    print(f"Successfully withdrawl")
    print(f"Account Balance is {Balance - amount}")
elif amount <=0:
    print("Invalid Amount ")
else:
    print("Insufficient Balance ")
print("Thank you , Visit again ")
