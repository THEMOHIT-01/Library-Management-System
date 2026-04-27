from utils import books,issued
def show():
    if not books:
        print("library is empty.\n")
    else:
        print("Book in library: ")
        for book,qty in books.items():
            print(f"{book} : {qty}")
        print()    