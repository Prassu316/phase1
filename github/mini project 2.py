#create a class ticket which will bw thw abstract class inside that create a function book ticket
#which will be the abstract method and has nothing in it.create a class make my trip which will
#use the book ticket function class to take the details such as name ,phno,email,jour date,and displace a message
#thankyou for booking in make my trip.create a class irctc which uses the book ticket of ticket
#class and same details as make my trip.but in the end it will give an option to user to select wheather it is one way or round trip,
#if the user option is roundtrip it again asak the user to return the return date as well and then print
#a message thanks to choose irctc else thanks for choosing irctc.create a class indigo which takes
#all the detais as irctc and just asks which mode of transport you want.
from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def bookticket(self):
        pass
class makemytrip(ticket):
    def bookticket(self):
        self.name=input("enter your name:")
        self.phno=input("enter phone number:")
        self.email=input("enter email id:")
        self.date=input("enter journey date:")
        print("tthankyou for booking in makemytrip")
class irctc(ticket):
    def bookticket(self):
        self.name=input("enter your name:")
        self.phno=input("enter phone number:")
        self.email=input("enter email id:")
        self.date=input("enter journey date:")
        print("1.oneway,2.roundtrip")
        while True:
            self.trip=input(" ")
            if(self.trip=="oneway" or self.trip=="1" or self.trip=="roundtrip" or self.trip=="2"):
                break
            else:
                print("invalid input")
        if(self.trip=="roundtrip"):
            self.retdate=input("enter return date:")
            print("thankyou for booking in irctc")
        else:
            print("tthankyou for booking in irctc")
class indigo(ticket):
    def bookticket(self):
        self.name=input("enter your name:")
        self.phno=input("enter phone number:")
        self.email=input("enter email id:")
        self.date=input("enter journey date:")
        print("1.oneway,2.roundtrip")
        while True:
            self.trip=input(" ")
            if(self.trip=="oneway" or self.trip=="1" or self.trip=="roundtrip" or self.trip=="2"):
                break
            else:
                print("invalid input")
        if(self.trip=="roundtrip" or self.trip=="2"):
            self.retdate=input("enter return date:")
        while True:
            print("1.train,2.bus,3.flight")
            self.mode=input(" ")
            if(self.mode=="train" or self.mode=="1" or self.mode=="bus" or self.mode=="2" or self.mode=="flight" or self.mode=="3"):
                break
            else:
                print("invalid input")
        print("thankyou for booking in indigo")
print("1.makemytrip,2.irctc,3.indigo")
while True:
            option=input(" ")
            if(option=="makemytrip" or option=="1"):
                obj=makemytrip()
                obj.bookticket()
            elif (option=="irctc" or option=="2"):
                obj1=irctc()
                obj1.bookticket()
            elif(option=="indigo" or option=="3"):
                obj2=indigo()
                obj2.bookticket()
            else:
                print("invalid input")

        
    
        
        
        
        
