#!/usr/bin/python3
"""Module that prints the id of the State matching a name argument."""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def get_state(username, password, db_name, state_name):
    """Print the id of the State named state_name, or Not found."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(State.name == state_name).order_by(
        State.id).all()
    found = [s for s in states if s.name == state_name]
    if found:
        print(found[0].id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    get_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
