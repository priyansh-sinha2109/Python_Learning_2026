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

#Question 7 :- 

n = int(input("Tell me the number :- "))

odd = 0
even = 0

for i in range(1 ,n+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print(f"your even or odd sum is {even} , {odd}")

#Question 8 :-

n = int(input("Please Enter the number :- "))

for i in range(1 , n+1):
    if n % i == 0:
        print(i)

# Question 9 :-

n = int(input("Enter the Perfect number :- "))

sum = 0

for i in range(1 , n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print(f"Hence the number is perfect")
else:
    print("Hence the number is not a perfect number")

#Question 10 :-

n = int(input("Enter the Perfect number :- "))

count = 0

for i in range(1 , n):
    if n % i == 0:
        count = count + 1

if count == 2:
    print(f"Hence the number is prime")
else:
    print("Hence the number is not a prime number")

#Question 11 :-

a = "SHERYIANS"

print(a[::-1])

#Question 12:-

a = "SHERYIANS"

b = ""

for i in range(len(a)-1 , -1 , -1):
    b = b + a[i]
    print(b)

if b == a:
    print("Hence number is palindrome")
else:
    print("Hence number is not Palindrome")