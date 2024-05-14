#!/usr/bin/python3
"""This updates a state"""

from sqlalchemy.orm import sessionmaker

import sys
from model_city import City, Base
from model_state import State, Base

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id)
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")
