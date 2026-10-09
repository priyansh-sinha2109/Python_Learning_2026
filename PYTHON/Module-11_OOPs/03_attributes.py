class Animal:
    name = "lion" # class attributes

    def __init__(self , age):
        self.age = age    #instance attributes

    def show(self):
        print("how are you")  #instance method

    @classmethod
    def hello(cls):    # target class not object
        print("how are you brother")

    @staticmethod    
    def static():  # target nothing
        print("how are you my boy")

obj = Animal(12)

obj.show()

obj.hello()

obj.static()