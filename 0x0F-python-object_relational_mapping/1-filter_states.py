#!/usr/bin/python3
"""This module states with a name starting with
 N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(user=username, password=password,
                         database=db_name, port=3306, host="localhost")
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE BINARY name LIKE
              'N%' ORDER BY id ASC""")
    data = c.fetchall()

    for row in data:
        print(row)
    db.close()
