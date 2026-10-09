class Factory:
    a = 12 # attribute

    def hello(self): #method
        print("Hello")

    print("Hello how are you i am getting initialized")

print(Factory().a)

Factory().hello()

obj = Factory()

print(obj.a)

obj.hello()