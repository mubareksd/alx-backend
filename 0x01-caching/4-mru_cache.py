#!/usr/bin/env python3
"""4-mru_cache module
"""
BasicCaching = __import__('base_caching').BaseCaching


class MRUCache(BasicCaching):
    """MRUCache class
    """
    def __init__(self):
        """__init__ function
        """
        super().__init__()
        self.call = []

    def put(self, key, item):
        """put function

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key and item:
            if key not in self.cache_data:
                self.call.append(key)
            if len(self.call) > BasicCaching.MAX_ITEMS:
                rm_key = self.call.pop(-2)
                print("DISCARD: {}".format(rm_key))
                del self.cache_data[rm_key]
            self.cache_data[key] = item

    def get(self, key):
        """get function

        Args:
            key ([type]): [description]

        Returns:
            [type]: [description]
        """
        if key in self.cache_data:
            self.call.remove(key)
            self.call.append(key)
            return self.cache_data[key]
        return None
