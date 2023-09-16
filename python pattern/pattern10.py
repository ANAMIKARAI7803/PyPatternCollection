n= int(input('enter number rows of no.'))
for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(j),end=" ")
    for j in range (i - 65 , 0 ,-65):
        print(chr(j),end=" ")
    print()
