import sqlite3

FILENAME = "data/todo.db"


def create():
    # """CREATE TABLE todo (ID INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(125) NOT NULL, comment VARCHAR(200), status INTEGER DEFAULT 0, create_at datetime DEFAULT (datetime('now', 'localtime')));"""

    title = input("Title: ")
    comment = input("Comment: ")

    with sqlite3.connect(FILENAME) as connection:
        cursor_ = connection.cursor()
        cursor_.execute(
            """INSERT INTO todo (title, comment) VALUES (?, ?);""", (title, comment)
        )

        print("Succes, create to-do.")


def read():
    with sqlite3.connect(FILENAME) as connection:
        cursor_ = connection.cursor()
        cursor_.execute("""SELECT * FROM todo;""")
        rows = cursor_.fetchall()

        for row in rows:
            print(
                f"ID: {row[0]} | Title: {row[1]} | Comment: {row[2]} | Status: {row[3]}, Create_at: {row[4]}"
            )


def update():
    with sqlite3.connect(FILENAME) as connection:
        cursor_ = connection.cursor()

        while True:
            try:
                id = int(input("ID: "))
                break
            except ValueError:
                print("Xato, butun son kiriting.")

        cursor_.execute("""SELECT * FROM todo;""")
        rows = cursor_.fetchall()
        for row in rows:
            if row[0] == id:
                print(
                    f"ID: {row[0]} | Title: {row[1]} | Comment: {row[2]} | Status: {row[3]}, Create_at: {row[4]}"
                )

        choise = input("Update to-do (yes/no): ").strip().lower()
        if choise == "yes":
            title = input("Title: ")
            comment = input("Comment: ")

            cursor_.execute(
                """UPDATE todo SET title = ?, comment = ? WHERE id = ?;""",
                (title, comment, id),
            )

        print("Succes update to-do")


def delete():
    with sqlite3.connect(FILENAME) as connection:
        cursor_ = connection.cursor()

        while True:
            try:
                id = int(input("ID: "))
                break
            except ValueError:
                print("Xato, butun son kiriting.")

        cursor_.execute("""SELECT * FROM todo;""")
        rows = cursor_.fetchall()

        for row in rows:
            if row[0] == id:
                print(
                    f"ID: {row[0]} | Title: {row[1]} | Comment: {row[2]} | Status: {row[3]}, Create_at: {row[4]}"
                )

                choise = input("Delete to-do (yes/no): ").strip().lower()

                if choise == "yes":
                    cursor_.execute("""DELETE FROM todo WHERE id = ?;""", (id,))

                    print("Succes, delete to-do.")


def check():
    with sqlite3.connect(FILENAME) as connection:
        cursor_ = connection.cursor()

        while True:
            try:
                id = int(input("ID: "))
                break
            except ValueError:
                print("Xato, butun son kiriting.")

        cursor_.execute("""SELECT * FROM todo;""")
        rows = cursor_.fetchall()

        for row in rows:
            if row[0] == id:
                print(
                    f"ID: {row[0]} | Title: {row[1]} | Comment: {row[2]} | Status: {row[3]}, Create_at: {row[4]}"
                )

                if row[3] == 1:
                    status = 0
                else:
                    status = 1

                choise = (
                    input(f"({row[1]}) {status} qilasizmi? (yes/no): ").strip().lower()
                )
                if choise == "yes":
                    cursor_.execute(
                        """UPDATE todo SET status = ? WHERE id = ?;""", (status, id)
                    )

                    print("Succes, check to-do.")
