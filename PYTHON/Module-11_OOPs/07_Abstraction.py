from abc import ABC , abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        print("perimeter")

    @abstractmethod
    def area(self):
        print("area")


class Square(abstract):
    def __init__(self , side):
        self.side = side
    def perimeter(self):
        return super().perimeter()
    def area(self):
        return super().area()

class circle(abstract):
    def __init__(self , radius):
        self.radius = radius

    def perimeter(self):
        return super().perimeter()  
    
    def area(self):
        return super().area()

obj = circle(12)
obj = Square(12)

obj.area()