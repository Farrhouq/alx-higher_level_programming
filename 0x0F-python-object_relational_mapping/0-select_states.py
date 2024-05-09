#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(user=username, password=password, database=db_name, port=3306, host="localhost")
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY id ASC""")

