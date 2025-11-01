class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Publication:
    def __init__(self, no_rp, no_book, no_art):
        self.no_rp = no_rp
        self.no_book = no_book
        self.no_art = no_art


class Faculty(Person, Publication):
    def __init__(self, name, age, gender, desig, dept, no_rp, no_book, no_art):
        # initialize both parent classes
        Person.__init__(self, name, age, gender)
        Publication.__init__(self, no_rp, no_book, no_art)
        self.desig = desig
        self.dept = dept

    def display(self):
        print("Name of faculty:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Designation:", self.desig)
        print("Department:", self.dept)
        print("No of research papers published:", self.no_rp)
        print("No of book chapters published:", self.no_book)
        print("No of articles published:", self.no_art)


# -------- Main Program --------
f1 = Faculty("Pooja Sinha", 48, "Female", "HOD", "CSE", 5, 2, 3)
f1.display()
