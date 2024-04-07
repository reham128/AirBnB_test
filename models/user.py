#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.place import Place
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
