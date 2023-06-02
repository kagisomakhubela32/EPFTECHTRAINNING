
v1 = 0
v2 = 1
v3 = 0
sum = 0

for i in range(10):
    v3 = v1 + v2
    print(v1)

    v3 = v3 + v1
    next = v1 + v2
    v1 = v2
    v2 = next

    if v1 % 2 == 0:
        s = s + v1

print(s)




print(sum)
