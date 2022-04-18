k = 0
m = 0
c = []
for i in range(1107, 9505):
    if i % 9 == 0 and i % 7 != 0 and i % 15 != 0 and i % 17 != 0 and i % 19 != 0:
        k += 1
        c.append(i)
print(k, min(c))