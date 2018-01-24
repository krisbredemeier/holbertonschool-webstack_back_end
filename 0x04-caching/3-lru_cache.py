#!/usr/bin/python3
'''
implements least recently used caching
'''
from base_caching import BaseCaching
import datetime


class LRUCache(BaseCaching):
    '''class that inherits from BaseCaching '''

    def __init__(self):
        '''Constructor'''
        super().__init__()
        self.cache_data = {}
        self.lst = []
        self.time = 0
        self.lru = {}

    def get(self, key):
        if key not in self.cache_data:
            return None
        if key in self.cache_data:
            self.lru[key] =self.time
            self.time += 1
            return self.cache_data[key]

    def put(self, key, item):
        if len(self.cache_data) >= self.MAX_ITEMS:
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache_data.pop(old_key)
            self.lru.pop(old_key)
            print("DISCARD: {}".format(key))
        self.cache_data[key] = item
        self.lru[key] = self.time
        self.time +=1

    @property
    def size(self):
        '''return size of cache_data'''
        return len(self.cache_data)
