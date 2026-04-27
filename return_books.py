from utils import *

def return_():
    book_name=input("enter book you want to return : ").lower()
    person_name=input("Enter your name: ")
    qty=int(input("enter the no of book to return : "))
    found=False
    
    for record in issued:
        if record["book"]==book_name and record["name"]==person_name:
            found=True
            issue_date=record["date"]
            today=datetime.now()

            days=(today-issue_date).days
            
            books[book_name]+=qty
            issued.remove(record)

            print(f"\n book returned by {person_name}")
            print(f"\n Days: {days}") 

            amount=0
            if days<=7:
                amount=10*days*qty
            elif  days<=14:
                amount+=20*days*qty
            elif  days<=21:
                amount+=30*days*qty  
            else:
                amount+=40*days*qty
            print("money to pay: ",amount)
                
            
            break


    
    if not found:
        if book_name not in books:
            print("this book not belong to my library\n")
        else:
            print("No record found for this person")
