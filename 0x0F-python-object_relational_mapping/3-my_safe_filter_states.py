#!/usr/bin/python3
"""This module states with a name searched from the database hbtn_0e_0_usa
safe from sql injections"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]
    db = MySQLdb.connect(user=username, password=password,
                         database=db_name, port=3306, host="localhost")
    c = db.cursor()

    sql_query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    c.execute(sql_query, (searched_name,))

    data = c.fetchall()

    for row in data:
        print(row)

    db.close()
