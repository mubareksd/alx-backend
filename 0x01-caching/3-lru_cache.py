#!/usr/bin/env python3
"""3-lru_cache module
"""
BasicCaching = __import__('base_caching').BaseCaching


class LRUCache(BasicCaching):
    """LIFOCache class
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
            if len(self.cache_data) > BasicCaching.MAX_ITEMS:
                print("DISCARD: {}".format(list(self.cache_data.keys())[0]))
                self.cache_data.pop(list(self.cache_data.keys())[0])

    def get(self, key):
        """get function

        Args:
            key ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.cache_data.get(
                key, None) if key in self.cache_data else None
