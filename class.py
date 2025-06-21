class hello:
    x=10
obj=hello()
print(obj.x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=person("adithyakrishna",21)
print(obj.name)
print(obj.age)

#inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self):
        print("My name is",self.name,"and im",self.age)
class employee(person):
    pass
obj=employee("jassim",20)
obj.sample()
