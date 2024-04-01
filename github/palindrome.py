n=int(input(""))
a=n
r=0
while(n>0):
    temp=n%10
    r=(r*10)+temp
    n=n//10
if r==a:
    print("true")
else:
    print("false")
