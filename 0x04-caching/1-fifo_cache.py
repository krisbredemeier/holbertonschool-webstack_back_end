#!/usr/bin/python3
from base_caching import BaseCaching
import datetime

class LIFOCache(BaseCaching):
    '''class that inherits from BaseCaching '''

    def __init__(self):
        '''Constructor'''
        self.cache_data = {}
        self.MAX_ITEMS = len(self.cache_data)

    def put(self, key, item):
        '''set max_items for caching'''
        current_len = len(self.cache_data)
        self.cache_data[key] = item
        if self.cache_data[key] is None or item is None:
            return
        if key not in self.cache_data and self.MAX_ITEMS >= current_len
            self.remove_last()

    def get(self, key):
        '''return value linked to key'''
        if key not in self.cache_data:
            return None
        if key is None:
            return None

    def remove_last(self):
        '''remove the last added entry'''
        last_entry = None
        for key in self.cache_data:
            if last_entry is None:
                last_entry = key
            elif self.cache_data[key][] < self.cache_data[last_entry][
            'last_entry']:
            last_entry = key
            self.cache_data.pop(last_entry)

    @property
    def size(self):
        '''return size of cache_data'''
        return len(self.cache_data)
