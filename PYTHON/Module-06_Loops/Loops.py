#For Loops

# a = range(1 , 21 , 3)
# a = range(21)
# a = range(20 , 51)
a = range(16 , -1 , -1)

for i in a:
    print(i)

#let's print a table

a = range(5 , 51 , 5)

for i in a:
    print(i)

a = "SHERYIANS IS A TEACHING PLATFORM"

# for i in range(len(a)):
#     print(a[i])

for i in a:
    print(i)

#Break & # continue

for i in range(1 , 21):
    if i == 15:
        # break
        continue

else:
    print(i)

# Questions


#Question 1:- 

a = int(input("Enter your number :- "))

for i in range(a):
    print("hello world")

#Question 2 :-

n = int(input("Enter your number :- "))

for i in range(1,n+1):
    print(i)

#Question 3 :- 

b = int(input("Enter your number :- "))

for i in range(b , 0 , -1):
    print(i)

#Question 4 :- 

num = int(input("Enter the number you want to it in table :- "))

for i in range(1 ,11):
    print(f"{num} * {i} = {num * i}")

#Question 5 :- 

add = int(input("Enter the number :- "))

count = 0

for i in range(1 , add + 1):
    count = count + i

print(f"Sum is {count}")


#Question 6 :-

fac = int(input("Enter the factorial number :- "))

mul = 1

for i in range(fac , 0 , -1):
    mul = mul * i

print(f"Factorial is {mul}")

