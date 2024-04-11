#!/usr/bin/env python3
""" BasicCache module
This module defines a BasicCache class that inherits from BaseCaching.
It implements a simple caching system without a limit on the number of items.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
    This class inherits from BaseCaching and implements
    a simple caching system.
    It does not have a limit on the number of items that can be stored.
    """

    def put(self, key, item):
        """ Add an item to the cache.
        This method assigns the item value to the key
        in the cache_data dictionary.
        If the key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key.
        This method returns the value associated with the key
        in the cache_data dictionary.
        If the key is None or does not exist in the cache_data,
        it returns None.
        """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
