class faculty:
    def __init__(self,fname,branch,f_id):
        self.fname=fname
        self.branch=branch
        self.f_id=f_id
    def infor(self):
        print("faculty information=",self.fname,self.branch,self.f_id)
class cseds(faculty):
    pass

obj=faculty("prasanna","cse-ds","4411")
obje=cseds("devi","ds","a4411")
obje.infor()
obj.infor()
