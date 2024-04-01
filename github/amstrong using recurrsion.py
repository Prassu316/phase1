def armstrong(n,a):
    if n==0:
        return 0
    temp=n//10
    return((n%10)**a+armstrong(temp,a))
def count(n):
    if n==0:
        return 0
    else:
        temp=n//10
        return(1+count(temp))
n=int(input(""))
a=count(n)
print(armstrong(n,a))
       
    
