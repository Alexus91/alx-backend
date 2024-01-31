#!/usr/bin/python3
"""
Module 4-mru_cache.py
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a MRU caching system """

    def __init__(self):
        """ Initializes the MRU cache """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.key_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.key_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """ Retrieves the item by key """
        if key in self.key_order:
            self.key_order.remove(key)
            self.key_order.append(key)
        return self.cache_data.get(key)
