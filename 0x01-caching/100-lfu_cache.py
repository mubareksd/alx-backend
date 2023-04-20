#!/usr/bin/env python3
"""100-lfu_cache module
"""
BasicCaching = __import__('base_caching').BaseCaching


class LFUCache(BasicCaching):
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
            if key not in self.call.keys():
                self.call[key] = 0
            if len(self.cache_data) > self.MAX_ITEMS:
                min_key = min(self.call, key=self.call.get)
                print('DISCARD: {}'.format(min_key))
                del self.cache_data[min_key]
                del self.call[min_key]

            self.cache_data[key] = item

    def get(self, key):
        """get function

        Args:
            key ([type]): [description]
        """
        if key in self.cache_data:
            self.call[key] += 1
            return self.cache_data[key]
        return None
