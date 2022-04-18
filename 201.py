import random as r

l = [r.randint(1000, 2000) for i in range(20)]
c = []
for i in range(len(l) - 1):
    if l[i] % 3 == 0 and l[i] % 5 != 0:
        c.append(l[i])
print(c)