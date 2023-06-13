
v1 = 1
v2 = 2
v3 = 0
sum = 0

while  sum  < 4000000:
    v3 = v1 + v2
    print(v1)

    v3 = v3 + v1
    next = v1 + v2
    v1 = v2
    v2 = next

    if v1 % 2 == 0:
        sum = sum + v1

print(sum)