#
num = 56
num2 = 0 
prim = 2
arr = []

while num > 1:
    if  num % prim == 0 :
        num2 = num / prim
        #print(prim)
        arr.append(prim)
        num = num2
    else:
        prim += 1

print(arr)