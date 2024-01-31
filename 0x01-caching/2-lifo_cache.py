#!/usr/bin/python3
"""
Module 2-lifo_cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a LIFO caching system """

    def __init__(self):
        """ Initializes the LIFO cache """
        super().__init__()

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last key inserted into the cache
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD:", last_key)
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key)
