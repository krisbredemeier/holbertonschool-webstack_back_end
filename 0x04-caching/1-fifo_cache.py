#!/usr/bin/python3
from base_caching import BaseCaching
import datetime

class FIFOCache(BaseCaching):
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
        if key not in self.cache_data and self.MAX_ITEMS >= current_len:
            self.remove_first()

    def get(self, key):
        '''return value linked to key'''
        if key not in self.cache_data:
            return None
        if key is None:
            return None

    def remove_first(self):
        '''remove the last added entry'''
        first_entry = None
        for key in self.cache_data:
            if first_entry is None:
                first_entry = key
            elif self.cache_data[key] < self.cache_data[first_entry][
            'first_entry']:
                first_entry = key
            self.cache_data.pop(first_entry)
            print("DISCARD:{key}")

    @property
    def size(self):
        '''return size of cache_data'''
        return len(self.cache_data)
