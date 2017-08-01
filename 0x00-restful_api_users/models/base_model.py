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

from datetime import datetime
from uuid import *

class BaseModel():

    id = None
    created_at = None
    updated_at = None

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
