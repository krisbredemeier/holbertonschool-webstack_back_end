#!/usr/bin/python3
from base_caching import BaseCaching
'''
test
'''

class BasicCache(BaseCaching):
    '''
    class that inherits from BaseCaching
    '''

    def __init__(self):
        '''Constructor'''
        self.cache_data = {}

    def put(self, key, item):
        ''' assign to dictionary'''
        if key is None or item is None:
            pass
        if not key or not item:
            pass
        self.cache_data[key] = item

    def get(self, key):
        '''return value linked to key '''
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
