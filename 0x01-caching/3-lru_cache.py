#!/usr/bin/python3
"""
Module 3-lru_cache.py
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defines a LRU caching system
    """

    def __init__(self):
        """initialize the LRU """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Assigns the item "
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.keys:
                del_key = self.keys.pop(0)
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """the item by key
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
