#!/usr/bin/env python3
"""LFUCache module This module defines a LFUCache class that inherits from
BaseCaching.

It implements a caching system using the LFU algorithm.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class This class inherits from BaseCaching and implements a
    caching system using the LFU algorithm."""

    def __init__(self):
        """Initialize the LFUCache.

        Calls the parent class's __init__ method.
        """
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """Add an item to the cache.

        This method assigns the item value to the key in the cache_data
        dictionary. If the key or item is None, this method does
        nothing. If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS, it discards the least frequency used
        item (LFU algorithm) and prints a discard message. If more than
        one item needs to be discarded, it uses the LRU algorithm to
        discard the least recently used.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.keys.remove(key)
                self.keys.append(key)
                self.uses[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_freq = min(self.uses.values())
                    candidates = [
                        k for k, v in self.uses.items() if v == min_freq]
                    if len(candidates) > 1:
                        # Use LRU to discard the least recently used among the
                        # candidates
                        discarded_key = candidates.pop(0)
                        del self.cache_data[discarded_key]
                        self.keys.remove(discarded_key)
                        del self.uses[discarded_key]
                    else:
                        # Discard the only candidate
                        discarded_key = candidates[0]
                        del self.cache_data[discarded_key]
                        del self.uses[discarded_key]
                    print("DISCARD: {}".format(discarded_key))
                self.cache_data[key] = item
                self.keys.append(key)
                # Initialize the frequency of the new key to 1
                self.uses[key] = 1

    def get(self, key):
        """Retrieve an item from the cache by key.

        This method returns the value associated with the key in the
        cache_data dictionary. If the key is None or does not exist in
        the cache_data, it returns None.
        """
        if key is not None:
            if key in self.cache_data:
                self.keys.remove(key)
                self.keys.append(key)
                # Increment the frequency of the accessed key
                self.uses[key] += 1
                return self.cache_data[key]
        return None
