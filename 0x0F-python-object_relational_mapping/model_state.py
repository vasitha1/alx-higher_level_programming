#!/usr/bin/python3
"""
This model creates a class base and linkes it to the database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

mymetadata = MetaData()
Base = declarative_base(mymetadata)

class State(Base):
   """
   Defines the base class
   """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
