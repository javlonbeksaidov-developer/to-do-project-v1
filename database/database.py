import sqlite3

FILENAME = "data/todo.db"


def create(command):
    connection = sqlite3.connect(FILENAME)
    cursor_ = connection.cursor()

    # """CREATE TABLE books (id, name, author, price);"""
    cursor_.execute(command)

    connection.commit()
    cursor_.close()


def read(command):
    pass


def update(command):
    pass


def delete(command):
    pass


def check():
    pass