#!/usr/bin/python3
from BaseModel import BaseModel

class User(BaseModel):

    def __init__(self):
        self.email = None
        self.first_name = None
        self.last_name = None
        self.__password = None
