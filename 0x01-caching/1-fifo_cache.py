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
        self.queue = deque([])

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.queue:
                del self.cache_data[self.queue.popleft()]
                print("DISCARD: {}".format(self.queue.popleft()))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key)
