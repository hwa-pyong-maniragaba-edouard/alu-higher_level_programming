#!/usr/bin/python3
"""Module that lists all states starting with N from a MySQL database."""
import sys

import MySQLdb


def filter_states(username, password, db_name):
    """Print all states whose name starts with N, sorted by states.id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                "ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
