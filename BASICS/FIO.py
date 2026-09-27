a=input('Enter contect to write :')
with open("abc.py","w") as f:
    f.write(a + "/n")
    print("text written succesfully")

b=input("Enter content to append :") 
with open("abc.py","a") as f:
    f.write(b + "/n")
    print("Appending is successfully  ")   

    print("\nFinal content is :")
    with open("abc.py","r") as f:
        v=f.read()
        print(v)
