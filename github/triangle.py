a=int(input("enter 1st side:"))
b=int(input("enter 2nd side:"))
c=int(input("enter 3rd side:"))
if (a==b==c):
    print("equilateral triangle")
elif (a==b)or(a==c)or(b==c):
    print("isosales triangle")
else:
    print("scaler triangle")
