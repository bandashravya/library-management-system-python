from datetime import datetime


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    # Add Book
    def add_book(self, book_id, book_name):
        self.books[book_id] = book_name
        print("Book added successfully.")

    # Show Books
    def show_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books")
            for book_id, book_name in self.books.items():
                print(f"Book ID: {book_id} | Book Name: {book_name}")

    # Remove Book
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed successfully.")
        else:
            print("Book ID not found.")

    # Borrow Book
    
    def borrow_book(self, book_id, student_id, student_name):
        if book_id in self.books:

            book_name = self.books.pop(book_id)

            issue_date = datetime.now().strftime("%d-%m-%Y")

            self.borrowed_books[book_id] = {
                "Book Name": book_name,
                "Student ID": student_id,
                "Student Name": student_name,
                "Issue Date": issue_date
            }

            print("Book borrowed successfully.")
            print("Issue Date:", issue_date)

        else:
            print("Book not available.")

    # Return Book
    def return_book(self, book_id):
        if book_id in self.borrowed_books:

            details = self.borrowed_books.pop(book_id)

            return_date = datetime.now().strftime("%d-%m-%Y")

            self.books[book_id] = details["Book Name"]

            print("Book returned successfully.")
            print("Student Name :", details["Student Name"])
            print("Return Date :", return_date)

        else:
            print("Book was not borrowed.")

    # Search Book
    def search_book(self, book_id):
        if book_id in self.books:
            print("Book Available")
            print(self.books[book_id])

        elif book_id in self.borrowed_books:
            print("Book is Borrowed")
            print("Borrowed By :", self.borrowed_books[book_id]["Student Name"])

        else:
            print("Book not found.")

    # Borrowed Books Details
    def borrowed_details(self):
        if len(self.borrowed_books) == 0:
            print("No borrowed books.")
        else:
            print("\nBorrowed Books")
            for book_id, details in self.borrowed_books.items():
                print("----------------------------")
                print("Book ID :", book_id)
                print("Book Name :", details["Book Name"])
                print("Student ID :", details["Student ID"])
                print("Student Name :", details["Student Name"])
                print("Issue Date :", details["Issue Date"])


library = Library()

# Initial Books
library.add_book(101, "Python")
library.add_book(102, "Java")
library.add_book(103, "C")
library.add_book(104, "HTML")


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1.Show Books")
    print("2.Add Book")
    print("3.Remove Book")
    print("4.Borrow Book")
    print("5.Return Book")
    print("6.Search Book")
    print("7.Show Borrowed Books")
    print("8.Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        library.show_books()

    elif choice == 2:
        book_id = int(input("Enter Book ID : "))
        book_name = input("Enter Book Name : ")
        library.add_book(book_id, book_name)

    elif choice == 3:
        book_id = int(input("Enter Book ID : "))
        library.remove_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter Book ID : "))
        student_id = input("Enter Student ID : ")
        student_name = input("Enter Student Name : ")
        library.borrow_book(book_id, student_id, student_name)

    elif choice == 5:
        book_id = int(input("Enter Book ID : "))
        library.return_book(book_id)

    elif choice == 6:
        book_id = int(input("Enter Book ID : "))
        library.search_book(book_id)

    elif choice == 7:
        library.borrowed_details()

    elif choice == 8:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
library.add_book(104,"HTML")
library.remove_book("C")
library.borrow_book(104,45607,"HARRY")
library.return_book("HTML")
library.search_book("Python")
library.search_book("C")
library.search_book("HTML")
library.search_book("java")
library.show(books)
        
               