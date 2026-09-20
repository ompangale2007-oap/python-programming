class Student:
    
    name = "A"
    lang = "JS"
    roll = 123

    
    def __init__(self, name="A", lang="JS", roll=123):
        self.name = name
        self.lang = lang
        self.roll = roll


ABC = Student() 
print(ABC.name)   
XYZ = Student("B", "Python", 456)
print(XYZ.name) 