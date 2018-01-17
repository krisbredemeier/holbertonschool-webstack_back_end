#!/usr/bin/python3
from base_caching import BaseCaching
import datetime
# import requests
# import requests_cache
#
# requests_cache.install_cache('cache_data')

class BasicCache(BaseCaching):
    '''
    class that inherits from BaseCaching
    '''

    def __init__(self):
        '''Constructor'''
        self.cache_data = {}


    def put(self, key, item):
        ''' assign to dictionary'''
        self.cache_data[key] = {'value': item}
        if self.cache_data[key] is None or item is None:
            return


    def get(self, key):
        '''return value linked to key '''
        if self.cashe_data[key] is None or key not in self.cache_data:
            return None
