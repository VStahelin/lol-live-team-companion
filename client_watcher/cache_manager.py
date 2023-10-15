import cachetools

cache = cachetools.LRUCache(maxsize=1000)


def set_cache(key, value):
    cache[key] = value


def get_cache(key):
    return cache.get(key)
