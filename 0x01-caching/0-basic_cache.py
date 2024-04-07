#!/usr/bin/env python3
"""
Clas that inherits from basic caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from basiccaching"""
    def put(self, key, item):
        """assigns a dict to an item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns self.cache"""
        return self.cache_data.get(key, None)
