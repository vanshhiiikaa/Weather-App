print("LIBRARY MANAGEMENT SYSTEM")
class Book:
    def __init__(self,bookid,bookname,authorname,category,availabilitystatus):
        self.bookid = bookid
        self.bookname = bookname
        self.authorname = authorname
        self.category = category
        self.availabilitystatus = availabilitystatus

    def show(self):
        print(f"Book ID: {self.bookid}")
        print(f"Book Name: {self.bookname}")
        print(f"Author Name: {self.authorname}")
        print(f"Category: {self.category}")
        print(f"Availability Status: {self.availabilitystatus}")
        print("****************")

    def update_status(self,new_status):
        self.availabilitystatus = new_status

class Member:
    def __init__(self,memberid,membername,contactdetails,borrowedbooks):
        self.memberid = memberid
        self.membername = membername
        self.contactdetails = contactdetails
        self.borrowedbooks = []

    def show(self):
        print(f"Member ID: {self.memberid}")
        print(f"Name: {self.membername}")
        print(f"Contact: {self.contactdetails}")
        print(f"Borrowed Books: {self.borrowedbooks}")
        print("****************")

    def borrow_book(self, book):
        self.borrowedbooks.append(book.bookname)
        book.update_status("Issued")

    def return_book(self, book):
        self.borrowedbooks.remove(book.bookname)
        book.update_status("Available")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.show()

    def add_member(self, member):
        self.members.append(member)

    def display_members(self):
        for member in self.members:
            member.show()

    def search_book(self, bookname):
        for book in self.books:
            if book.bookname == bookname:
                book.show()
                return
        print("Book not found")

    def issue_book(self, book, member):
        if book.availabilitystatus == "Available":
            member.borrow_book(book)
            print("Book issued successfully")
        else:
            print("Book is already issued")

    def return_book(self, book, member):
        member.return_book(book)
        print("Book returned successfully")

# Creating Books
book1 = Book(101, "Python Basics", "ABC", "Programming", "Available")
book2 = Book(102, "Java Basics", "XYZ", "Programming", "Available")

# Creating Members
member1 = Member(1, "Rahul", "9876543210", [])

# Creating Library
library1 = Library()

# Adding Books to Library
library1.add_book(book1)
library1.add_book(book2)

# Adding Member to Library
library1.add_member(member1)

# Display Books
print("\nALL BOOKS:")
library1.display_books()

# Display Members
print("\nALL MEMBERS:")
library1.display_members()

# Search Book
print("\nSEARCH RESULT:")
library1.search_book("Python Basics")

# Issue Book
print("\nISSUE BOOK:")
library1.issue_book(book1, member1)

library1.display_books()
member1.show()

# Return Book
print("\nRETURN BOOK:")
library1.return_book(book1, member1)

library1.display_books()
member1.show()