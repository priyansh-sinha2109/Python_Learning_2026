class Animal:
    def __init__(self , name , age):
        self.name = name 
        self.age = age

    def __str__(self):      #dunder method direct access for this function
        return "hello how are you"

    def __add__(self, other):
        sum = 0
        for i in other:
            sum = sum + i.age


        return f"your sum of ages are :- {self.age + sum} "

obj = Animal("lion" , 13)
obj2 = Animal("dolphin" , 12)
obj3 = Animal("tiger" , 34)

print(obj + (obj2 , obj3))