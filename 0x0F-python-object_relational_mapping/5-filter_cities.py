#!/usr/bin/python3
"""This module searches a name searched from the database hbtn_0e_0_usa
safe from sql injections"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched_state = sys.argv[4]
    db = MySQLdb.connect(user=username, password=password,
                         database=db_name, port=3306, host="localhost")
    c = db.cursor()
    query_string = """SELECT cities.name FROM cities JOIN states ON
              cities.state_id = states.id where states.name =
              %s ORDER BY cities.id ASC;"""

    c.execute(query_string, (searched_state,))
    data = c.fetchall()

    if data:
        for row in data[:-1]:
            print(f"{row[0]}, " , end='')
        print(data[-1][0])
    else:
        print()
    db.close()
