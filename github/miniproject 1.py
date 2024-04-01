#toyoto,mahindra,mercedes
#take the input from user for the car company name and in the input msg give the user
#the three companies this company name goes as input/arg/ to model name function,
#which welcomes the user accordingly to the company name .ask the user to enter the specific model
#name for that company
#the second function whose name is varient.according to the company name and car model then
#user should be asked to enter the varient he would like to chooose from petrol and diesel
#last display function according to the compsny car model name and car varient dirst its
#ex show room price will be displayed and then its on road price should be dislayed,which
#cal as ex show price+cgst+sgst+insurance
#sgst,cgst,insurance all the threee have common value throughout the car show room
class car:
    def __init__(self):
        print("car showroom")
        print("1.toyoto,2.mahindra,3.mercedes")
        while True:
            self.a=input(" ")
            if(self.a=="toyoto" or self.a=="mahindra" or self.a=="mercedes"):
                break
            else:
                print("invalid input")
        print("welcome to the",self.a,"family")
    def model(self):
        print("1.hyndai,2.gvegan,3.suzuki")
        while True:
            self.b=input(" ")
            if(self.b=="hyndai" or self.b=="gvegan" or self.b=="suzuki"):
                break
            else:
                print("invalid input")
        print ("your model no is",self.b)
    def varient(self):
        print("1.petrol,2.diesel")
        while True:
            self.c=input(" ")
            if(self.c=="petrol" or self.c=="diesel"):
                break
            else:
                print("invalid input")
        print("your",self.a,"car with model",self.b,"contains",self.c,"varient")
    def price(self):
        if(self.a=="toyoto"):
            if(self.b=="hyndai"):
                self.sp=200000
                self.cgst=(self.sp)*0.15
                self.sgst=(self.sp)*0.15
                self.insu=(self.sp)*0.15
                print(self.sp+self.cgst+self.sgst+self.insu)
            elif(self.b=="gvegan"):
                self.sp=250000
                self.cgst=(self.sp)*0.15
                self.sgst=(self.sp)*0.15
                self.insu=(self.sp)*0.15
                print(self.sp+self.cgst+self.sgst+self.insu)
            else:
                self.sp=180000
                self.cgst=(self.sp)*0.15
                self.sgst=(self.sp)*0.15
                self.insu=(self.sp)*0.15
                print(self.sp+self.cgst+self.sgst+self.insu)
        if(self.a=="mahindra"):
            if(self.b=="hyndai"):
                self.sp=200000
                self.cgst=(self.sp)*0.20
                self.sgst=(self.sp)*0.20
                self.insu=(self.sp)*0.20
                print(self.sp+self.cgst+self.sgst+self.insu)
            elif(self.b=="gvegan"):
                self.sp=250000
                self.cgst=(self.sp)*0.20
                self.sgst=(self.sp)*0.20
                self.insu=(self.sp)*0.20
                print(self.sp+self.cgst+self.sgst+self.insu)
            else:
                self.sp=180000
                self.cgst=(self.sp)*0.20
                self.sgst=(self.sp)*0.20
                self.insu=(self.sp)*0.20
                print(self.sp+self.cgst+self.sgst+self.insu)
        if(self.a=="mercedes"):
            if(self.b=="hyndai"):
                self.sp=200000
                self.cgst=(self.sp)*0.30
                self.sgst=(self.sp)*0.30
                self.insu=(self.sp)*0.30
                print(self.sp+self.cgst+self.sgst+self.insu)
            elif(self.b=="gvegan"):
                self.sp=250000
                self.cgst=(self.sp)*0.30
                self.sgst=(self.sp)*0.30
                self.insu=(self.sp)*0.30
                print(self.sp+self.cgst+self.sgst+self.insu)
            else:
                self.sp=180000
                self.cgst=(self.sp)*0.30
                self.sgst=(self.sp)*0.30
                self.insu=(self.sp)*0.30
                print(self.sp+self.cgst+self.sgst+self.insu)
obj=car()
obj.model()
obj.varient()
obj.price()

    
