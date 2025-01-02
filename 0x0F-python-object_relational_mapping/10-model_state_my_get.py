#!/usr/bin/python3

"""
This model lists all states in the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 5:
        print("Not found")
        return

    searched_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name == searched_name).first()
    if instance is None:
        print("Not found")
    else:
        print(instance.id)

    session.close()


if __name__ == "__main__":
    main()
