#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache evicts the least recently used item when full.
    """

    def __init__(self):
        """Initialize LRU cache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        Move key to end of usage_order (most recently used).
        Evict least recently used key if cache is full.
        """
        if key is None or item is None:
            return

        # If key is already in usage, remove it so we can re-add it to end
        if key in self.usage_order:
            self.usage_order.remove(key)

        # If cache is full and key is new, evict LRU
        if (key not in self.cache_data and
                len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        # Add to cache and mark as most recently used
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve item by key.
        Mark as most recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark key as most recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
