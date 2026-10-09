class Factory:
    def __init__(self , materials , zips , pockets):
        self.materials = materials
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"your object details are :- {self.materials} , {self.pockets} , {self.zips}")

reebok = Factory("leather" , 5 , 2)

campus = Factory("nylon" , 3 , 3)

print(reebok.pockets)
print(campus.pockets)

reebok.show()

