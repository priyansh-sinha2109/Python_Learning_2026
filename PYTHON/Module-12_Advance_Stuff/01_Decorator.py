class Animal:
    @property
    def show(self):
        print("hello how are you!!..")

obj = Animal()

obj.show

def decorate(func):
    def wrapper(*args , **Kwargs):
        print("the addition to your number")
        func(*args , **Kwargs)
        print("thankyou I hope you liked it")

    return wrapper


@decorate
def hello():
    print("Hello i am akash")

hello()


def addition(a,b):
    print(f"Your total is {a + b}")

addition(12 , 67 , 13 , 14)