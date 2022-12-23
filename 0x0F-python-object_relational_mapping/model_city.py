#!/usr/bin/python3
""" Setup a mappable table using SQLALCHEMY """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """ Map this class to a table """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column("state_id", Integer, ForeignKey("states.id"))
