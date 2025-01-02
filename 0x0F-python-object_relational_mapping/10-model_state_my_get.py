#!/usr/bin/python3

"""
This model lists all states in the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    searched_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name == (sys.argv[4],))
    if not instance:
        print("Not found")
    else:
        print(instance[0].id)


if __name__ == "__main__":
    main()
