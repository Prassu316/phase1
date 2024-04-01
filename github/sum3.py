n=1578
a=n
sum=0
count=0
while(n>0):
    n=n//10
    count=count+1
b=1
while(a>0):
    while(b<=count):
        temp=a%10
        sum=sum+(temp**count)
        a=a//10
        count=count-1
print(sum)
    
        
