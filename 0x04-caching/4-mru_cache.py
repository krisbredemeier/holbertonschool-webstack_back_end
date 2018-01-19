#!/usr/bin/python3
from base_caching import BaseCaching
import datetime


class MRUCache(BaseCaching):
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
            self.remove_most_recently_used()

    def get(self, key):
        '''return value linked to key'''
        if key not in self.cache_data:
            return None
        return self.cache_data[key]

    def remove_most_recently_used(self):
        '''remove the last added entry'''
        most_recently_used = None
        for key in self.cache_data:
            if most_recently_used is None:
                most_recently_used = key
            elif self.cache_data[key]['date_used'] > self.cache_data[most_recently_used]['date_used']:
                    most_recently_used = key
        self.cache_data.pop(most_recently_used)
        print("DISCARD: {}".format(most_recently_used))

    @property
    def size(self):
        '''return size of cache_data'''
        return len(self.cache_data)
