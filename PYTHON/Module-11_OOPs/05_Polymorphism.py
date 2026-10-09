class Animal:
    def show(self):
        print("hello i am akash")

class Human(Animal):
    def show(self):
        print("how are you")

obj = Human()

obj.show()