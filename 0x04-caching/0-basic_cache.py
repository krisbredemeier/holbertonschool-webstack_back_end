#!/usr/bin/python3
from base_caching import BaseCaching
import datetime


class BasicCache(BaseCaching):
    '''
    class that inherits from BaseCaching
    '''

    def put(self, key, item):
        self.cache_data[key] = {'value': item}
        if self.cache_data[key] is None or item is None
            return
    def get(self, key):
        if self.cashe_data[key] is None or key not in self.cache_data:
            return None


    
