
class programmer:
    company = "MS"

    def __init__(self, name, Id, post):
        self.name = name
        self.Id = Id
        self.post = post

p = programmer("A", 233, "Software Engineer")
print(p.name, p.Id, p.company, p.post)

q = programmer("B", 234, "Senior Developer")
print(q.name, q.Id, q.company, q.post)
                
        