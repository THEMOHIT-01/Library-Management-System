from utils import *

def issue():
    book_name = input("Enter book name to issue: ").lower()
    if book_name in books:
        if books[book_name]>0:
            qty=int(input("enter no of books: "))
            person_name=input("Enter your name: ")
            date=datetime.now()
            books[book_name]-=qty
            issued.append({"book":book_name,"name":person_name,"date":date})
            print(f"Book issued to {person_name} on {datetime}\n ")
        else:
            print("Book out of stock!\n")
    else:
        print("book not found in library")
        