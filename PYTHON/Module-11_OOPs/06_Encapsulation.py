class factory:
    __a = "pune"

    def __show(self):
        print("hello i am pune factory")

obj = factory()

# obj.a = "Bhopal"

# print(obj.a)

class Bhopal(factory):
    def show(self):
        print(super().__a)


obj = Bhopal()

obj.show()