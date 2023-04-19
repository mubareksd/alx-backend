#!/usr/bin/env python3
"""1-fifo_cache module
"""
BasicCaching = __import__('base_caching').BaseCaching


class FIFOCache(BasicCaching):
    """FIFOCache class
    """
    def __init__(self):
        """__init__ function
        """
        super().__init__()

    def put(self, key, item):
        """put function

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(list(self.cache_data.keys())[0]))
            del self.cache_data[list(self.cache_data.keys())[0]]

    def get(self, key):
        """get function

        Args:
            key ([type]): [description]
        """
        return self.cache_data.get(key) if key in self.cache_data else None
