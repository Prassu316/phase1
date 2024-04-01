l=[22,-1,42,65,1,-4,6]
temp=0
min=0
for i in range(len(l)-1):
    if (l[i]<temp):
        temp=l[i]
        if temp<min:
            temp=min
            min=l[i]
print(temp)
