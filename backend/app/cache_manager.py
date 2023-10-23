import cachetools

cache = cachetools.LRUCache(maxsize=1000)


def set_cache(key, value):
    cache[key] = value


def get_cache(key):
    return cache.get(key)


def update_cache(key, new_value):
    if key in cache:
        cache[key] = new_value
    else:
        set_cache(key, new_value)


def add_to_cached_dict(key, new_key, value):
    try:
        cached_dict = get_cache(key)
        cached_dict[new_key] = value
        cache[key] = cached_dict

    except TypeError:
        cache[key] = {new_key: value}


def remove_from_cached_dict(key, remove_key):
    try:
        cached_dict = get_cache(key)
        if remove_key in cached_dict:
            del cached_dict[remove_key]
            cache[key] = cached_dict

    except TypeError:
        pass
