#!/usr/bin/python3
""" 4. MRU Caching
"""
from datetime import datetime
from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Defines a LFU caching system """

    def __init__(self):
        """ Initializes the LFU cache """
        super().__init__()
        self.frequency = {}
        self.access_time = {}

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            least_frequent_keys = [
                    k for k, v in self.frequency.items() if v == min_freq]

            if len(least_frequent_keys) > 1:
                lru = min(self.access_time, key=lambda k: self.access_time[k])
                least_frequent_keys = [lru]

            for discard_key in least_frequent_keys:
                del self.cache_data[discard_key]
                del self.access_time[discard_key]
                del self.frequency[discard_key]
                print("DISCARD:", discard_key)

        self.cache_data[key] = item
        self.access_time[key] = datetime.now()
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Retrieves the item by key """
        element = self.cache_data.get(key)
        if element:
            self.access_time[key] = datetime.now()
            self.frequency[key] += 1
        return element
