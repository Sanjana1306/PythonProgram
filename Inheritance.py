class dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
        
    def display(self):
        print(self.name)
        print(self.breed)
        print(self.age)
        

class cat(dog):
    def __init__(self,name,breed,color,age):
        self.name=name
        self.breed=breed
        self.color=color
        
        dog.__init__(self,name,breed,age)
    def details(self):
        print(self.name)
        print(self.breed)
        print(self.color)
        
        

g=cat('Tommy','giant','green',12)

g.display()

g.details()



