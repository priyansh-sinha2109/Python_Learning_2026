a = [12 , 13 ,14]

# 1st way  using index in list traversing

for i in range(len(a)):
    print(a[i]) 

# 2nd way direct in list traversing

for i in a:
    print(i)

# print(dir(list))

# Method

l = [2,3,4,5,6,7]

l.append(9)
l.insert(2, 10)
l.remove(2)
l[0] = 10


print(l)

#Question :-

l = [-45 , 10 , -90 , 80]

print("ALl Positive number are:-")
for i in l:
    if i >= 0:
        print(i)

print("ALl Negative number are:-")
for i in l:
    if i <= 0:
        print(i)

#Question :-

l = [12, 13 , 14 , 15]

sum = 0

for i in l:
    sum = sum + i

print(sum/ len(l))

#Question :-

l = [100 , 12 , 256 , 257 , 100 , 300]

greatest = l[0]
index = 0
for i in range(len(l)):
    if greatest < l[i]:
        greatest = l[i]
        index = i

print(greatest , index)

#Question :-

l = [100 , 12 , 256 , 257 , 100 , 300]

largest = l[0]
sLargest = l[0]
index_largest = 0
index_sLargest = 0

for i in range(len(l)):
    if l[i] > largest:
        sLargest = largest
        index_largest = index_sLargest
        largest = l[i]
        index_sLargest = i
    elif i > sLargest:
        sLargest = i

print(f"{largest} , {sLargest} , largest index =  {index_sLargest} , second largest index =  {index_largest}")


#Question :- 

a = [13 , 14 , 15 , 17 ]

for i in range(len(a) - 1):
    if a[i] < a[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")

