"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""
from sqlite3 import connect


con = connect("my_db.sqlite")
c = con.cursor()

# c.execute("CREATE TABLE login(username VARCHAR, password VARCHAR, PRIMARY KEY(username))")
# c.execute("INSERT INTO login values('admin1', 'Password')")
# c.execute("INSERT INTO login values('admin2', 'Nbv12345')")

# c.execute("CREATE TABLE info(name VARCHAR, age INT)")
# c.execute("INSERT INTO info values('Maneesh', 23)")
# c.execute("INSERT INTO info values('Sowmya', 26)")
c.execute("INSERT INTO info values(?, ?)", ("Aanchal", 23,))

c.execute("SELECT * FROM login")
print(c.fetchall())

c.execute("SELECT * FrOM info")
print(c.fetchall())

con.commit()
con.close()
