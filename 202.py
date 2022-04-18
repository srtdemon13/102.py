import random as r

l = [r.randint(1000, 2000) for i in range(20)]
ch = []
notch = []
for i in range(len(l) - 1):
    if i % 2 == 1:
        notch.append(l[i])
    else:
        ch.append(l[i])
f = sum(notch)
s = sum(ch)
if f > s:
    print('On odds side live more people')
elif s > f:
    print('On even side live more people')
else:
    print('same')
print(f)
print(s)