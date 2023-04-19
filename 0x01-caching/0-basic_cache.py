#!/usr/bin/env python3
"""0-basic_cache module
"""
BasicCaching = __import__('base_caching').BaseCaching


class BasicCache(BasicCaching):
    """BasicCache class
    """
    def put(self, key, item):
        """put function

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get function

        Args:
            key ([type]): [description]

        Returns:
            [type]: [description]
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
