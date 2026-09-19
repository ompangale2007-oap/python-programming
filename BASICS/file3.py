word = "for"
with open ("for.py","r") as f:
    content=f.read()
    CONTENT = content.replace(word,"FOR")
    with open ("for.py","w") as f:
        f.write(CONTENT)
