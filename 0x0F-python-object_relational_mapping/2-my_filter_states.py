#!/usr/bin/python3
"""This module states with a name searched from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]
    print(searched_name)

    db = MySQLdb.connect(user=username, password=password,
                         database=db_name, port=3306, host="localhost")
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE '{}'
              ORDER BY id ASC""".format(searched_name))
    data = c.fetchall()

    for row in data:
        print(row)
    db.close()
