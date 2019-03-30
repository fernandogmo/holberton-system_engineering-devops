#!/usr/bin/python3
"""
SQL Injection safe version of `2-my_filter_states.py`.
Takes in an argument and displays all values in the `states`
table of `hbtn_0e_0_usa` where `name` matches the argument.
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    name = (argv[4],)

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    cursor.execute(("SELECT * FROM states "
                    "WHERE name=%s "
                    "ORDER BY id"), name)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
