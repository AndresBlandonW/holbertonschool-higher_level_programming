#!/usr/bin/python3
"""takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name='{}' ORDER BY cities.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in range(len(rows)):
        print(rows[row][0], end='')
        if row < len(rows) - 1:
            print(', ', end='')
    print()

    cur.close()
    db.close()
