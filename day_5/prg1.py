class Library:
    # class variables
    tb = 0
    tu = 0
    tp = 0

    def __init__(self, b_name=None, b_price=0, u_name=None):
        self.b_name = None
        self.b_price = 0
        self.u_name = None

        # Case 1: Book is added
        if b_name is not None and b_name != "":
            self.b_name = b_name
            self.b_price = b_price
            Library.tb += 1
            Library.tp += b_price

        # Case 2: User is added
        elif u_name is not None and u_name != "":
            self.u_name = u_name
            Library.tu += 1

    def display_book_details(self):
        if self.b_name:
            print("Book Name:", self.b_name, ", Price:", self.b_price)

    def display_user_details(self):
        if self.u_name:
            print("User Name:", self.u_name)


# ---------- Main Program ----------
books = []
users = []

# Input for books
n = int(input("Enter number of books: "))
for i in range(n):
    bname = input("Enter name of book " + str(i+1) + ": ")
    bprice = float(input("Enter price of book " + str(i+1) + ": "))
    books.append(Library(b_name=bname, b_price=bprice))

# Input for users
m = int(input("\nEnter number of users: "))
for i in range(m):
    uname = input("Enter name of user " + str(i+1) + ": ")
    users.append(Library(u_name=uname))

# Displaying book details
print("\n---- Book Details ----")
for book in books:
    book.display_book_details()

# Displaying user details
print("\n---- User Details ----")
for user in users:
    user.display_user_details()

# Displaying totals
print("\n---- Library Summary ----")
print("Total Books:", Library.tb)
print("Total Users:", Library.tu)
print("Total Price of Books:", Library.tp)