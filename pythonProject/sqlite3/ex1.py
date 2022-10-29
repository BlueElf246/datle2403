import sqlite3
conn=sqlite3.connect('chinook.db')
c=conn.cursor()
# c.execute("""CREATE TABLE employee(
#         first text,
#         last text,
#         pay integer
#         )""")
#c.execute("INSERT INTO employee VALUES('dat','le','2000')")

c.execute("SELECT * from tracks")
print(c.fetchmany(5))
conn.commit()
conn.close()