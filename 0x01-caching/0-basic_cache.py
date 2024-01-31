#!/usr/bin/python3
"""
Module 0-basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Defines a basic caching system """

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the value associated with the given key """

        return self.cache_data.get(key)
