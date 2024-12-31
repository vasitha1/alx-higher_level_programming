#!/usr/bin/python3
"""
This model creates a class base and linkes it to the database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
   """
   Defines the state class to represent the base table
   """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
