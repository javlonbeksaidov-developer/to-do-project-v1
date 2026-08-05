from database.database import check, create, delete, read, update
from menu.menu import start_menu


def main():
    while True:
        print(start_menu())
        choise = input(">>> ")
        if choise == "0":
            break
        elif choise == "1":
            create()
        elif choise == "2":
            read()
        elif choise == "3":
            update()
        elif choise == "4":
            delete()
        elif choise == "5":
            check()

if __name__ == "__main__":
    main()
