#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    cursor.close()
    db.close()
