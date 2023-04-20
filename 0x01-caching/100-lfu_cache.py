#!/usr/bin/env python3
"""100-lfu_cache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class
    """
    def __init__(self):
        """__init__ function
        """
        super().__init__()
        self.call = {}

    def put(self, key, item):
        """put function

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_key = min(self.call, key=self.call.get)
                print("DISCARD: {}".format(min_key))
                del self.cache_data[min_key]
                del self.call[min_key]
            if key not in self.call.keys():
                self.call[key] = 0
            else:
                self.call[key] += 1

    def get(self, key):
        """get function

        Args:
            key ([type]): [description]
        """
        if key is None or key not in self.cache_data:
            return None
        self.call[key] += 1
        return self.cache_data.get(key)
