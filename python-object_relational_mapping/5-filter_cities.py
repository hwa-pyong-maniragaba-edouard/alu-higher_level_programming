#!/usr/bin/python3
"""Module that lists all cities of a given state from a MySQL database."""
import sys

import MySQLdb


def filter_cities(username, password, db_name, state_name):
    """Print all cities of state_name on one line, sorted by cities.id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = BINARY %s "
                "ORDER BY cities.id ASC", (state_name,))
    print(", ".join(row[0] for row in cur.fetchall()))
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
