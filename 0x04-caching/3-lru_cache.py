#!/usr/bin/python3
from base_caching import BaseCaching
import datetime


class LRUCache(BaseCaching):
    '''class that inherits from BaseCaching '''

    def __init__(self):
        '''Constructor'''
        super().__init__()

    def put(self, key, item):
        '''set max_items for caching'''
        self.cache_data[key] = {
            'item': item,
            'date_used': datetime.datetime.now()
            }
        current_len = len(self.cache_data)
        if key is None or item is None:
            pass
        if self.MAX_ITEMS < current_len:
            self.remove_last_used()

    def get(self, key):
        '''return value linked to key'''
        if key not in self.cache_data:
            return None
        if key is None:
            return None
        return self.cache_data[key]

    def remove_last_used(self):
        '''remove the last added entry'''
        last_used = None
        for key in self.cache_data:
            if last_used is None:
                last_used = key
            elif self.cache_data[key]['date_used'] < self.cache_data[last_used]['date_used']:
                    last_used = key
        self.cache_data.pop(last_used)
        print("DISCARD: {}".format(last_used))

    @property
    def size(self):
        '''return size of cache_data'''
        return len(self.cache_data)
