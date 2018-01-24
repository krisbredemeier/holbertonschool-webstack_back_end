#!/usr/bin/python3
'''
implements first in first out caching
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''class that inherits from BaseCaching '''

    def __init__(self):
        '''Constructor'''
        super().__init__()
        self.cache_data = {}
        self.lst = []

    def put(self, key, item):
        '''set max_items for caching'''
        if not key or not item:
            pass
        if key not in self.cache_data:
            self.lst.append(key)
        self.cache_data[key] = item
        if len(self.lst) > self.MAX_ITEMS:
            remove = self.lst.pop(0)
            del self.cache_data[remove]
            print("DISCARD: {}".format(remove))

    def get(self, key):
        '''return value linked to key'''
        if key not in self.cache_data:
            return None
        return self.cache_data[key]

    @property
    def size(self):
        '''return size of cache_data'''
        return len(self.cache_data)
