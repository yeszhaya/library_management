# Library Management System

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email


class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.active = True


class LibraryService:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []

    # 1. Add Book
    def add_book(self):
        print("\n--- Add New Book ---")
        book_id = input("Input Book ID: ")
        title = input("Input Book Title: ")
        author = input("Input Book Author: ")
        
        new_book = Book(book_id, title, author)
        self.books[book_id] = new_book
        
        print(f"Output: 'Book added: {title}'")

    # 2. Register Member
    def register_member(self):
        print("\n--- Register New Member ---")
        member_id = input("Input Member ID: ")
        name = input("Input Member Name: ")
        email = input("Input Member Email: ")
        
        new_member = Member(member_id, name, email)
        self.members[member_id] = new_member
        
        print(f"Output: 'Member registered: {name}'")

    # 3. Borrow Book
    def borrow_book(self):
        print("\n--- Borrow Book ---")
        book_id = input("Input Book ID: ")
        member_id = input("Input Member ID: ")

        # Check if book exists
        book = self.books.get(book_id)
        if not book:
            print("Raise BookNotFoundError: 'Book not found.'")
            print("Output: Error message")
            return

        # Check if member exists
        member = self.members.get(member_id)
        if not member:
            print("Raise MemberNotFoundError: 'Member not found.'")
            print("Output: Error message")
            return

        # Check if book is available
        if not book.available:
            print("Raise BookAlreadyBorrowedError: 'Book is already borrowed.'")
            print("Output: Error message")
            return

        # Process borrowing
        new_loan = Loan(book, member)
        self.loans.append(new_loan)
        book.available = False
        
        print(f"Output: 'Member {member.name} borrowed {book.title}.'")

    # 5. View Books
    def view_books(self):
        print("\n--- View All Books ---")
        books_list = list(self.books.values())

        if not books_list:
            print("Output: 'No books found.'")
            return

        print("Output: 'Books:' header")
        for book in books_list:
            status = "Available" if book.available else "Borrowed"
            print(f"Output: '{book.book_id} - {book.title} by {book.author} [{status}]'")
        print("more books? NO")

    # 6. View Members
    def view_members(self):
        print("\n--- View All Members ---")
        members_list = list(self.members.values())

        if not members_list:
            print("Output: 'No members found.'")
            return

        print("Output: 'Members:' header")
        for member in members_list:
            print(f"Output: '{member.member_id} - {member.name} ({member.email})'")
        print("more members? NO")

    # 7. View Loans
    def view_loans(self):
        print("\n--- View All Loans ---")
        if not self.loans:
            print("Output: 'No loans found.'")
            return

        print("Output: 'Loans:' header")
        for loan in self.loans:
            status = "Active" if loan.active else "Closed"
            print(f"Output: '{loan.book.book_id} - {loan.member.name} borrowed {loan.book.title} [{status}]'")
        print("more loans? NO")


def main():
    library = LibraryService()

    while True:
        print("\n======================================")
        print("      LIBRARY MANAGEMENT SYSTEM      ")
        print("======================================")
        print("[1] Add Book")
        print("[2] Register Member")
        print("[3] Borrow Book")
        print("[5] View Books")
        print("[6] View Members")
        print("[7] View Loans")
        print("[8] Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.register_member()
        elif choice == "3":
            library.borrow_book()
        elif choice == "5":
            library.view_books()
        elif choice == "6":
            library.view_members()
        elif choice == "7":
            library.view_loans()
        elif choice == "8":
            print("Output: 'Program closed.'")
            print("System exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()