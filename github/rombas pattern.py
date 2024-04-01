for i in range(1,5):
    for s in range(1,4-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
for i in range(3,0,-1):
    for s in range(0,4-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        print("*",end=" ")
    print()
