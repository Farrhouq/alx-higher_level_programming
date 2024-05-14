#!/usr/bin/python3
"""This fetches all states with a in their name"""

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
    insts = session.query(State).filter(State.name.like('%a%'))
    if not insts:
        print("Nothing")
    else:
        for inst in insts:
            print(f"{inst.id}: {inst.name}")
