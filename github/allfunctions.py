def val():
    print("i am a student")
val()
def val(a,b):
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")
val(141,170)
def val(name="uday",place="hyd"):
    print("i am ",name,"from",place)
val()
val("kasi","kkd")
def val(**name):
    print("my name is",name["fname"],"from",name["lname"])
val(fname="student",lname="kpd")
