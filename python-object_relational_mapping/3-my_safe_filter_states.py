#!/usr/bin/python3
"""Module that safely lists states matching a name given as an argument."""
import sys

import MySQLdb


def safe_filter_states(username, password, db_name, state_name):
    """Print all states matching state_name, safe from SQL injection."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = BINARY %s "
                "ORDER BY id ASC", (state_name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
