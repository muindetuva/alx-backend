#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that discards the most
    recently used item when the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """Initialize MRU cache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        Discard the most recently used item if cache is full.
        """
        if key is None or item is None:
            return

        if key in self.usage_order:
            self.usage_order.remove(key)

        # Cache full and new key → evict MRU (last used)
        if (key not in self.cache_data and
                len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.usage_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve item by key.
        Mark key as most recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
