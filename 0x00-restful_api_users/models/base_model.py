#!/usr/bin/python3

from datetime import datetime

class BaseModel():
    id = None
    created_at = None
    updated_at = None
    def __init__(self):
        self._id = str(UUID)
        self._created_at = datetime.utcnow()
        self._updated_at = datetime.utcnow()
