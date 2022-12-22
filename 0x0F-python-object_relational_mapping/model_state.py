#!/usr/bin/python3
""" Setup a mappable table using SQLALCHEMY """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ Map this class to a table """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128))
