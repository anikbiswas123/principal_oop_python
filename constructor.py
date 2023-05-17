# craete a class using constructor

class student:
    def __init__(self, name, dept, Roll):
        self.name = name
        self.dept = dept
        self.Roll = Roll

    def show(self):
        print("student name :"+self.name,"Department :"+self.dept)


std = student('anik', "CSE", 5465)
std.show()
