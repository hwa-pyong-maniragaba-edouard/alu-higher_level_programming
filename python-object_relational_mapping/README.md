# python-object_relational_mapping

This project links Python and MySQL. It uses MySQLdb to connect to a MySQL
database and run SQL queries, and later SQLAlchemy as an ORM to map Python
classes to database tables.

## Requirements

- Ubuntu 20.04 LTS, python3 (3.8.5)
- MySQL 8.0
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- pycodestyle 2.7.*

## Files

- `0-select_states.py`: lists all states from the database `hbtn_0e_0_usa`,
  sorted by `states.id`. Takes 3 arguments: mysql username, mysql password
  and database name.
