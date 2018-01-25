#!/usr/bin/python3
'''
implements most recenelty used caching
'''
from base_caching import BaseCaching
import datetime


class MRUCache(BaseCaching):
    '''class that inherits from BaseCaching '''

    def __init__(self):
        '''Constructor'''
        super().__init__()
        self.cache_data = {}
        self.lst = []
        self.time = 0
        self.mru = {}

    def get(self, key):
        '''set last used stamp starting from 0 for each item used '''
        if key not in self.cache_data:
            return None
        if key in self.cache_data:
            self.mru[key] = self.time
            '''keep track of when key was used'''
            self.time += 1
            return self.cache_data[key]

    def put(self, key, item):
        '''pop out item that is most recently used '''
        if len(self.cache_data) >= self.MAX_ITEMS:
            '''return the max of old_key arguments'''
            old_key = max(self.mru.keys(), key=lambda k: self.mru[k])
            self.cache_data.pop(old_key)
            self.mru.pop(old_key)
            print("DISCARD: {}".format(old_key))
        self.cache_data[key] = item
        self.mru[key] = self.time
        self.time += 1

    @property
    def size(self):
        '''return size of cache_data'''
        return len(self.cache_data)
