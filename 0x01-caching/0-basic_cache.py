#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    It has no limit — stores everything in a dictionary.
    """

    def put(self, key, item):
        """
        Add an item in the cache_data dictionary.
        Do nothing if key or item is None.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or doesn't exist.
        """
        return self.cache_data.get(key, None)
