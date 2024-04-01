n=int(input(" "))
a=n
sum=0
while(a>0):
    temp=a%10
    sum=sum+temp
    a=a//10
if(n%sum==0):
    print("true")
else:
    print("false")
