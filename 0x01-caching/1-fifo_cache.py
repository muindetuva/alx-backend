#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that removes the oldest
    item (first-in) when the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """Initialize cache with FIFO behavior"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, do nothing.
        If cache exceeds limit, discard oldest item (FIFO).
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.queue.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

    def get(self, key):
        """
        Retrieve item by key.
        Return None if key is None or not found.
        """
        return self.cache_data.get(key, None)
