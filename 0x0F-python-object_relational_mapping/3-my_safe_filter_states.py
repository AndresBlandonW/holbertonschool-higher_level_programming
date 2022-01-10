#!/usr/bin/python3
"""displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name=%s\
            ORDER by states.id ASC"
    cur.execute(sql, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
