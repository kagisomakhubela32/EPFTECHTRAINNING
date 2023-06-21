for i in range(2,600851475143):
    if 600851475143 % i == 0:
        for x in range(2,i):
            if i % x == 0:
                break
            else:
                prim = i
        print(prim)
