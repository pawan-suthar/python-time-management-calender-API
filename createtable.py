import sqlite3

conn = sqlite3.connect(f'time.db')
conn = conn.cursor()
print("database opened")

conn.execute(''' CREATE TABLE time
        (DATE DATE NOT NULL,
        CATAGORY TEXT NOT NULL,
        HOURS INT NOT NULL);''')

print("table created ")
