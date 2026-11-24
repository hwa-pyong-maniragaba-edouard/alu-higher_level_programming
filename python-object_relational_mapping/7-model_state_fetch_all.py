#!/usr/bin/python3
"""Module that lists all State objects from the database hbtn_0e_6_usa."""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def fetch_all_states(username, password, db_name):
    """Print all State objects sorted by states.id ascending."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    fetch_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
