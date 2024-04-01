def count(n):
    if n==0:
        return 0
    else:
        new=n//10
        return (1+count(new))
n=int(input(""))
print(count(n))
    
