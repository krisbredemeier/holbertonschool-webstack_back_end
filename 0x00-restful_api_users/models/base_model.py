#!/usr/bin/python3

'''
First, write a class named BaseModel. This defines the parent model
for all our future models.

Public class attributes:
id initialized to None
created_at initialized to None
updated_at initialized to None
Public instance methods:
def __init__(self) (override the instance creation method):
assign to id the string representation of an unique identifier
(please use the module uuid and the method uuid4())
assign to created_at and updated_at the current date and time in UTC
(please refer to the datetime module)
'''

from sqlalchemy import Column, Integer, String, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import *

Base = declarative_base()

# define basemodel
class BaseModel(object):

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())

    #create init for basemodel
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
