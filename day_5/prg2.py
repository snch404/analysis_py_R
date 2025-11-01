class Student:
    # class variables
    colg_name = "HITK"
    std_count = 0

    def __init__(self, stid, name, m1, m2, m3):
        self.stid = stid
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.average = (m1 + m2 + m3) / 3.0
        self.grade = self.calculate_grade()
        Student.std_count += 1

    def calculate_grade(self):
        if self.average >= 90:
            return 'O'
        elif self.average < 90 and self.average > 80:
            return 'A'
        elif self.average < 80 and self.average >= 70:
            return 'B'
        elif self.average < 70 and self.average >= 60:
            return 'C'
        elif self.average < 60 and self.average >= 50:
            return 'D'
        else:
            return 'F'

    def display(self):
        # print student info in tabular format
        print(self.stid, "\t", self.name, "\t", self.m1, "\t", self.m2, "\t", self.m3, "\t", 
              round(self.average, 2), "\t", self.grade)


# -------- Main Program --------
students = []

n = int(input("Enter total number of students: "))

for i in range(1, n+1):
    print("\nEnter details of Student", i)
    stid = i
    name = input("Enter name: ")
    sub1 = int(input("Enter marks in Subject 1: "))
    sub2 = int(input("Enter marks in Subject 2: "))
    sub3 = int(input("Enter marks in Subject 3: "))
    students.append(Student(stid, name, sub1, sub2, sub3))

# Printing output
print("\nCollege Name:", Student.colg_name)
print("Total Numbers of Students are:", Student.std_count)
print()
print("ID\tName\tSub1\tSub2\tSub3\tAverage\tGrade")

for s in students:
    s.display()
