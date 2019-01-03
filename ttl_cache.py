#!/usr/bin/env python3

import functools
import pickle
import time


def cache(ttl, typed=False, ignore_error=False):
    """Time To Live Cache
    Decorator to wrap a function with a memoizing callable that has TTL result
    """

    def wrap(fn):
        _tmp = {}

        @functools.wraps(fn)
        def fn_wrapped(*args, **kwargs):
            result = _tmp  # fake identifier
            now = time.monotonic()
            key = pickle.dumps(args) + pickle.dumps(kwargs)
            if key in _tmp:
                cd, result = _tmp[key]
                if cd > now:
                    return result

            try:
                result = fn(*args, **kwargs)
            except Exception:
                if ignore_error and result is not _tmp:
                    return result
                raise  # no previous result in _tmp

            _tmp[key] = now + ttl, result
            return result

        return fn_wrapped

    if callable(ttl):
        fn, ttl = ttl, 60.0
        return wrap(fn)

    ttl = float(ttl)

    return wrap


if __name__ == '__main__':
    @cache
    def test_1():
        pass
    @cache(5)
    def test_2():
        pass
    @cache(10, ignore_error=True)
    def test_3():
        pass
    @cache(1)
    def test(*args, **kwargs):
        print(test, args, kwargs)
    test(9, z=99)
    time.sleep(0)
    test(9, z=99)  # cached
    time.sleep(1)
    test(9, z=99)
else:
    from sys import modules
    self = modules[__name__]
    modules[__name__] = self.cache
