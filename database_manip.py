import sqlite3

# PS, again the file path is set up for my folders. Make sure it is set up to your system.
# I'll just catch all exceptions for this first task with SQLite

try:
    # Set up the DB and Cursor
    db = sqlite3.connect('./task 12/student_db')
    cursor = db.cursor()

    # Create the Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS python_programming (
                   id INTEGER PRIMARY KEY,
                   name TEXT(55),
                   grade INTEGER)''')
    print("Table has been created.")
    db.commit()

    # Create a list of tuples
    student_information = [(55,'Carl Davis',61),
                           (66,'Dennis Fredrickson',88),
                           (77,'Jane Richards',78),
                           (12,'Peyton Sawyer',45),
                           (2,'Lucas Brooke',99)]

    # Add all data to the table
    cursor.executemany('''
        INSERT INTO python_programming(id, name, grade)
        VALUES(?,?,?)''', student_information)
    print("All data added.")
    db.commit()


    # Print all data of the desired students to the terminal in a nice manner
    cursor.execute('''
        SELECT *
        FROM python_programming
        WHERE grade BETWEEN ? AND ?''', (60, 80))

    print("All data on students with a grade between 60 and 80:")
    print("")

    for row in cursor:
        print("-----------------------------")
        print(f"ID - {row[0]}\nName - {row[1]}\nGrade - {row[2]}")
        print("-----------------------------")
    print("")


    # Change the grade on a person named Carl
    person1 = 'Carl Davis'
    cursor.execute('''
        UPDATE python_programming
        SET grade = ?
        WHERE name = ?''', (65, person1))
    print(f"Grade updated for {person1}")
    db.commit()


    # Delete a specific user
    cursor.execute('''
        DELETE FROM python_programming
        WHERE name = 'Dennis Fredrickson'
    ''')
    print("Dennis Fredrickson, has been deleted from the table.")
    db.commit()


    # Change grades for ids under 55 (ps I'll just make them 100 since the pdf does not specify what to change them to?)
    cursor.execute('''
        UPDATE python_programming
        SET grade = 100
        WHERE id < 55''')
    print("Grades updated")
    db.commit()


    # Delete the whole table when done
    cursor.execute('''
        DROP TABLE python_programming''')
    print("Table has been deleted")
    db.commit()

except Exception as err:
    # Roll back if error occurs
    db.rollback()
    raise err

finally:
    # Close db connection
    db.close()
    print("Connection to the db has been disconnected")
    print("")

"""
Cites:
I do not have any cites for this one, I just have prior knowledge from a previous course I took.
"""

# https://www.youtube.com/watch?v=xvFZjo5PgG0
# ^ One important vid 💜
