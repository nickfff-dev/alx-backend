#!/usr/bin/env python3
"""LIFOCache module This module defines a LIFOCache class that inherits from
BaseCaching.

It implements a caching system using the LIFO algorithm.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class This class inherits from BaseCaching and implements a
    caching system using the LIFO algorithm."""

    def __init__(self):
        """Initialize the LIFOCache.

        Calls the parent class's __init__ method.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item to the cache.

        This method assigns the item value to the key in the cache_data
        dictionary. If the key or item is None, this method does
        nothing. If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS, it discards the last item put in
        cache (LIFO algorithm) and prints a discard message.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discarded_key = self.keys.pop()
                    del self.cache_data[discarded_key]
                    print("DISCARD: {}".format(discarded_key))
                self.cache_data[key] = item
                self.keys.append(key)

    def get(self, key):
        """Retrieve an item from the cache by key.

        This method returns the value associated with the key in the
        cache_data dictionary. If the key is None or does not exist in
        the cache_data, it returns None.
        """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
