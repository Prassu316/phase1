def rev(n):
    if(n==0):
        return
    print(n%10)
    return rev(n//10)

n=int(input(""))
rev(n)
