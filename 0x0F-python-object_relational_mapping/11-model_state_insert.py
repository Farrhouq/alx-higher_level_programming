#!/usr/bin/python3
"""This adds a new state"""

from sqlalchemy.orm import sessionmaker

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
