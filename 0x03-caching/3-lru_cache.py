#!/usr/bin/python3
"""LIFO Cache System Module"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """A LRU Cache System Class inherited from BaseCaching class
    Args:
        cache_data: dictionary representing cache
    """
    def __init__(self):
        self.counter = 0
        self.ages = {}
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for k, _ in sorted(self.ages.items(), key=lambda x: x[1]):
                self.cache_data.pop(k)
                self.ages.pop(k)
                break
            print('DISCARD:', k)
        if key:
            self.ages[key] = self.counter
            self.counter += 1


    def get(self, key):
        """Get an item from cache by key"""
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            return self.cache_data.get(key)
        else:
            return None

