minmlt = 0
minmlt1 = 0
temp = 1
while minmlt > 0:
    for i in range(1,20):
        if minmlt % i == 0:
           temp = minmlt
           minmlt = temp
 
        else:
            minmlt +=1

        print(minmlt)
