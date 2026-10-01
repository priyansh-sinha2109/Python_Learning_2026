def hello():
    print("Hello Function")

hello()

def sum(a , b):
    print(a + b)

sum(2,4)

def introduction(name , age):
    print(f"your name is {name} and your age is {age}")

introduction(name = "Priyansh" , age = 20)


def palindrome(st):
     rev = ""
     for i in range(len(st) -1 , -1 , -1):
        rev = rev + st[i]

     if rev == st:
        print("Plaindrome")
     else:
        print("not a plaindrome")

palindrome("NAMAN")
palindrome('GAURAV')


def hello():
    return ("hello how are you")

print(hello())