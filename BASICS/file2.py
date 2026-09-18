f=open("for.py")
content = f.read()
if("for " in content):
    print("The word for is present in the file")
else:
     print("The word for is not present in the file")
     f.close()