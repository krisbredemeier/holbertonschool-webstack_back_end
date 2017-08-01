#!/usr/bin/python3

from datetime import datetime
from uuid import *

class BaseModel():
    id = None
    created_at = None
    updated_at = None
    def __init__(self):
        self.id = uuid4()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
