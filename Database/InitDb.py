"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""
from sqlite3 import connect


con = connect("my_first_db.sqlite")
c = con.cursor()

# c.execute("CREATE TABLE login(username VARCHAR, password VARCHAR, PRIMARY KEY(username))")

# c.execute("INSERT INTO login values('admin1', 'Password')")
# c.execute("INSERT INTO login values('admin2', 'Nbv12345')")
usr = input("Enter username: ")
pwd = input("Enter password: ")
c.execute("SELECT * FROM LOGIN WHERE USERNAME=? AND PASSWORD=?", (usr, pwd))
logged = c.fetchall()
print(logged)
con.commit()
con.close()
