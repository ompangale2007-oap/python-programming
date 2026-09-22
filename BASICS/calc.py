class calc:
    def __init__(self,n):
        self.n=n
    def sq(self):
            print(f"The square is {self.n*self.n}")
    def cube(self):
                print(f"The cube is {self.n*self.n*self.n}")
    def sqr(self):
                print(f"The square root is {self.n**0.5}")
n=int(input("Enter n : "))
a=calc(n)
a.sq()
a.cube()
a.sqr()
