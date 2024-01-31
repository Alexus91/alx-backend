#!/usr/bin/python3
"""
Module 1-fifo_cache.py
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
    Defines a FIFO caching system
    """

    def __init__(self):
        """Initializes the FIFO cache"""
        super().__init__()

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key)
