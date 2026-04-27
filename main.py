from add_books import add
from show_books import show
from issue_books import issue
from return_books import return_

def library():
    while True:
        print("\n1. Add book")
        print("\n2. Show book")
        print("\n3. Issue book")
        print("\n4. Return book")
        print("\n5. Exit")

        choice=input("enter your choice : ")
        if choice.isdigit():
            choice=int(choice)
            if choice==1: add()
            elif choice==2: show()
            elif choice==3: issue()
            elif choice==4: return_()
            elif choice==5: 
                print("Thannk You")
                break
            else:
                print("Invalid choice..!!")
        else:
            print("Invalid choice..!!")
            
library()