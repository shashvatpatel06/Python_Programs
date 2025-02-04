import random
lst = [random.randrange(0,30) for _ in range(0,50)]
print(lst)
n=1
for i in range(0,50):
    if(n in lst):
        lst.remove(n)
        lst.append(n)
    n+=1
print(lst)

