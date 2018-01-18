#!/usr/bin/python3
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    class that inherits from BaseCaching
    '''

    def __init__(self):
        '''Constructor'''
        self.cache_data = {}

    def put(self, key, item):
        ''' assign to dictionary'''
        self.cache_data[key] = item
        if self.cache_data[key] is None or item is None:
            pass

    def get(self, key):
        '''return value linked to key '''
        if key not in self.cache_data:
            return None
        if key is None:
            return None
        return self.cache_data[key]
