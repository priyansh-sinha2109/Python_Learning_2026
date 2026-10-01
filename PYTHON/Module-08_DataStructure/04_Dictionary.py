d = {1 : "hello" , 2 : 56}  # Keys never be changed but value are changable

print(type(d))

d= {10:100 , 20 : 200 , 30 :300 , 40 :400}

print(d[10])

#Crud operation :-

d[10] = 1000

print(d[10])

#creation :-

#1st way :-

d.update({50:500})
print(d[50])

#2nd way :-
d[50] = 700 # updating
d[60] = 600 # creating
del d[30] # deleting

print(d)

#Traversing

d= {10:100 , 20 : 200 , 30 :300 , 40 :400}

for i in d:
    print(i , d[i])

# help(dict)

#Questin 1 :- 
d1 = {1 : 100 , 2 : 200 , 3 : 300 , 4 :400}
d2 = {10 : 1000 , 20 : 2000 , 30 : 3000 , 40 :4000}

for i in d2:
    d1[i] = d2[i] # creating

print(d1)

#Question 2 :-

d1 = {1 : 100 , 2 : 200 , 3 : 300 , 4 :400}

sum = 0
for i in d:
   sum += d[i]

print(sum)

#Question 3 count freq in list :-

d1 = [1,2,2,2,2,2,3,4,4 ,5 ]
d = {}

for i in d1:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1

print(d)

#Question 4 :- 

d1 = {1 : 100 , 2 : 200 , 3 : 300 , 4 :400}
d2 = {10 : 1000 , 20 : 2000 , 30 : 3000 , 40 :4000}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]