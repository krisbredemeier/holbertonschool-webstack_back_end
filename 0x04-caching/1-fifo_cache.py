#!/usr/bin/python3
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''class that inherits from BaseCaching '''

    def __init__(self):
        '''Constructor'''
        super().__init__()

    def put(self, key, item):
        '''set max_items for caching'''
        current_len = len(self.cache_data)
        self.cache_data[key] = item
        if key is None or item is None:
            pass
        if not key or not item:
            pass
        if self.MAX_ITEMS < current_len:
            self.remove_first()

    def get(self, key):
        '''return value linked to key'''
        if key not in self.cache_data:
            return None
        return self.cache_data[key]

    def remove_first(self):
        '''remove the last added entry'''
        first_entry = list(self.cache_data)[0]
        self.cache_data.pop(first_entry)
        print("DISCARD: {}".format(first_entry))

    @property
    def size(self):
        '''return size of cache_data'''
        return len(self.cache_data)
