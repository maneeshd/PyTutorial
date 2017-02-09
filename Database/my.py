"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""
from sqlite3 import connect


def get_days_remaining(ip):
    con = connect("my_first_db.sqlite")
    c = con.cursor()
    c.execute("select DAYS from first where IP=?", (ip,))
    days_left = c.fetchone()[0]
    con.close()
    return days_left


def delete_ip_from_list(ip):
    con = connect("my_first_db.sqlite")
    c = con.cursor()
    c.execute("delete from first where IP=?", (ip,))
    print("IP deleted..")
    con.commit()
    con.close()
    return 0


def is_deletable(ip):
    days = get_days_remaining(ip)
    if days < 1:
        delete_ip_from_list(ip)
    else:
        print("Days Remaining: %s" % str(days))
        days -= 1
        con = connect("my_first_db.sqlite")
        c = con.cursor()
        c.execute("UPDATE first SET DAYS=? where IP=?", (days, ip))
        con.commit()
        con.close()

if __name__:
    is_deletable("10.126.141.113")
