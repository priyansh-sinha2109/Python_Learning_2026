# l = []
# for i in range(1 , 21):
#     if i%2 == 0:
#         l.append(i)

# print(l)

l = [i for i in range(1 , 21) if i %2 == 0]

print(l)

l = {i : i **2 for i in range(1 , 10)}

print(l)
