n=int(input(" "))
a=n
temp=0
for i in range(1,int(n/2)):
    if(n%i==0):
        temp=temp+1
if(a>temp):
    print("true")
else:
    print("false")
    
