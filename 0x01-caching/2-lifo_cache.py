#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that discards the most
    recently added item (Last-In First-Out) when the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """Initialize LIFO cache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, do nothing.
        If cache is full, remove the last inserted item.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()  # Most recent key
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        # Remove existing key to re-append it (avoid duplicates)
        if key in self.stack:
            self.stack.remove(key)

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve item by key.
        Return None if key is None or not found.
        """
        return self.cache_data.get(key, None)
