n=int(input(" "))
a,b=n,n
temp=0
sum=0
count=0
while(n>0):
    n=n//10
    count=count+1
while(a>0):
    temp=a%10
    sum=sum+(temp**count)
    a=a//10
if(b==sum):
    print("true")
else:
    print("false")
