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
                ssr = sorted(self.call.items(), key=lambda x: x[1])
                print('DISCARD: {}'.format(ssr[0][0]))
                del self.cache_data[ssr[0][0]]
                del self.call[ssr[0][0]]

            self.cache_data[key] = item

    def get(self, key):
        """get function

        Args:
            key ([type]): [description]
        """
        if key in self.cache_data:
            if key not in self.call.keys():
                self.call[key] = 0
            self.call[key] += 1
            return self.cache_data[key]
        return None
