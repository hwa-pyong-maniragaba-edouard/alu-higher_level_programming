#!/usr/bin/python3
"""Module that lists states matching a name given as an argument."""
import sys

import MySQLdb


def filter_states_by_name(username, password, db_name, state_name):
    """Print all states whose name matches state_name, sorted by id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' "
                "ORDER BY id ASC".format(state_name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
