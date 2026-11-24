#!/usr/bin/python3
"""Module that lists all cities with their state from a MySQL database."""
import sys

import MySQLdb


def list_cities(username, password, db_name):
    """Print all cities and their state names, sorted by cities.id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
