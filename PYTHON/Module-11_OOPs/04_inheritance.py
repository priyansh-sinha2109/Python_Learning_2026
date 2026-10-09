class Factorymumbai:
    a = 12
    def hello(self):
        print("hello")


class Factorypune(Factorymumbai):  #child class / subclass
    pass


obj = Factorymumbai()
obj2 = Factorypune()


obj2.hello()


#

class Animal:
    def __init__(self , name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name , age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"hello your name is {self.name} , {self.age}")
        
animal1 = Animal("Lion")
person1 = Human("akarsh" , 12)


animal1.show()
person1.show()

#Single inheritence

# All the inheritence we saw is single inheritence

#Multiple inheritence

class Animal:
    name1 = "lion"


class Human:
    name2 = "harsh"

class Robots(Animal , Human):
    name3 = "Charlie123"

obj = Robots()

print(obj.name1)
print(obj.name2)
print(obj.name3)