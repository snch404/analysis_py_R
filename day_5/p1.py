class Student:
    collegeName = 'HITK'
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print('This method from Student class ')
        print(Student.collegeName)
        print(self.name)
        print(self.age)

class newstudent(Student):
    def __init__(self, name, age,marks):
        Student.__init__(self, name, age)
        self.marks=marks
    def display1(self):
        print('This method from newStudent class ')
        print(Student.collegeName)
        print(self.name)
        print(self.age)
        print(self.marks)


std = Student("Suraj Kumar", 25)
std.display()
#std.display1()
s1=newstudent("Ram",12,90)
s1.display1()
s1.display()