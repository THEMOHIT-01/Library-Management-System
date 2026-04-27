from utils import *

def add():
    book_name=input("Enter the book name: ").lower()
    qty=int(input("Enter no of books: "))
    if book_name in books:
        books [book_name]+=qty
    else:
        books[book_name]=qty

    print(book_name,"added successfully")
