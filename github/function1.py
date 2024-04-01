#create a class of name placements which has a function info which displays "we have
#create another calss name dept with function display which will display the names od the department presennt in the college
#create a class pragati with a function welcome which displays the message "welcome t
#this pragati class should aslo display the details about departments and placements.
class placements:
    def placements(self):
        print("we have 655 placements and stilll counting")
class department:
    def department(self):
        print("our departments are cse\nds\nai\naiml\nit\nece\nmech\neee\ncivil\ncs")
class pragati(department,placements):
    print("welcome to worst college in andhrapradesh")
    pass
obj2=pragati()
obj2.placements()
obj2.department()
