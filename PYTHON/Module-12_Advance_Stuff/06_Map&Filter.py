a = [1,2,3,4,5]

def double(x):
    return  x * 2

result = map(lambda x : x * 2 , a)

print(list(result))

print(double(a))



def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

a = [1 ,2 ,3 , 4 , 5]

result = filter(even , a)

print(list(result))