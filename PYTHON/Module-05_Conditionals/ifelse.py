a = 11

if a > 12:
    print("hello")

else:
    print("I will do this task")


money = int(input("please provide me the money :- "))

if money == 10:
    print("I will buy chocobar")

elif money == 20:
    print("I will have a mango dolly")

else:
    print("I will buy cone")


gen = input("Please tell you Gender as Character(M or F) :- ")

if gen == 'M' or gen == 'm':
    print("Good Morning Sir")

elif gen == 'F' or gen == 'f':
    print("Good morning mam")

else:
    print("Unidentified gender")

#Question

num = int(input("Enter your number :- "))

if num % 2 == 0:
    print("Number is even")
else:
    print("numeber is odd") 

name = input("Enter the name:- ")
age = int(input ("Enter your age :- "))

if age > 18:
    print(f"{name} you are eligible to vote")

else:
    print(f"{name} You are not eligible")


year = int(input("Tell me the exact year :- "))

if year % 100 == 0 and year % 400:
    print("It's a leap year")

elif year % 100 != 0 or year % 4 == 0:
    print("It's a leap year")

else:
    print("its a normal year")


t = int(input("Please tell the temperature :- "))

if t < 0:
    print("Freezing cold")

elif t>= 0 and t<10:
    print("very cold")

elif t>= 10 and t<20:
    print("cold")

elif t>= 20 and t<30:
    print("pleasent")

elif t>= 30 and t<40:
    print("hot")

else:
    print("temprature is hot")
    