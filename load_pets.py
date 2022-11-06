import sqlite3

def Person():

    Person = (
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    )

    con = sqlite3.connect('Person.db')

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS Person")
        cur.execute("CREATE TABLE Person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
        cur.executemany("INSERT INTO Person VALUES(?, ?, ?, ?)", Person)


def Pet():

    Pet = (
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    )

    con = sqlite3.connect('Pet.db')

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS Pet")
        cur.execute("CREATE TABLE Pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
        cur.executemany("INSERT INTO Pet VALUES(?, ?, ?, ?, ?)", Pet)

def Person_Pet():

    Person_Pet = (
        (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)
    )

    con = sqlite3.connect('Person_Pet.db')

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS Person_Pet")
        cur.execute("CREATE TABLE Person_Pet(person_id INTEGER, pet_id INTEGER)")
        cur.executemany("INSERT INTO Person_Pet VALUES(?, ?)", Person_Pet)

if __name__ == '__main__':
    Person()
    Pet()
    Person_Pet()
