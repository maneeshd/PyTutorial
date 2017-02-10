"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 10-Feb-17
"""
from sqlite3 import connect
from threading import Thread, Lock


def write_db(thread: str, name: str, age: int):
    print("[INFO] %s acquiring write lock on database..." % thread)
    db_lock.acquire()
    print("[INFO] %s writing database data..." % thread)
    cur.execute("INSERT INTO info VALUES(?, ?)", (name, int(age),))
    print("[INFO] %s finished writing database data..." % thread)
    print("[INFO] %s releasing write lock on database..." % thread)
    db_lock.release()


def read_db(thread: str):
    print("[INFO] %s acquiring read lock on database..." % thread)
    db_lock.acquire()
    print("[INFO] %s reading database data..." % thread)
    cur.execute("SELECT * FROM info")
    print("\t%s" % cur.fetchall())
    print("[INFO] %s releasing read lock on database..." % thread)
    db_lock.release()


def main():
    t1 = Thread(target=read_db, name="Thread-1", args=("Thread-1", ))
    t2 = Thread(target=write_db, name="Thread-2", args=("Thread-2", "T2", 27))
    t3 = Thread(target=write_db, name="Thread-3", args=("Thread-3", "T3", 3))
    t4 = Thread(target=read_db, name="Thread-4", args=("Thread-4", ))
    t5 = Thread(target=read_db, name="Thread-5", args=("Thread-5", ))
    t6 = Thread(target=write_db, name="Thread-6", args=("Thread-6", "T6", 45))

    threads = [t1, t2, t3, t4, t5, t6]

    for thread in threads:
        thread.start()
    t6.join()
    write_db("MainThread", "Main", 77)
    read_db("MainThread")
    print("[INFO] MainThread Exited")

if __name__ == '__main__':
    db_lock = Lock()
    with connect("my_db.sqlite", check_same_thread=False) as db:
        cur = db.cursor()
        cur.execute("DELETE FROM info")
        main()
