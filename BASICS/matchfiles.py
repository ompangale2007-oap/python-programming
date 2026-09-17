with open ("file1.py") as f:
    content = f.read()
    with open ("file2.py") as f:
        CONTENT= f.read()
        if content==CONTENT:
            print("both are equal ")
        else:
            print('are not equal ')