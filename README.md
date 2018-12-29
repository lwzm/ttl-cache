# ttl-cache

### How to use it

```sh
pip install ttl-cache
```

```python
import ttl_cache


# use ttl_cache directly
@ttl_cache
def expensive_operation(a, b):
    ...
    ...
    return SOME_RESULT

expensive_operation(xx, yy)
expensive_operation(xx, yy)  # prefer cached result
# ... 60 seconds later
expensive_operation(xx, yy)  # compute again


# or
@ttl_cache(2.0)  # cache the result in the next 2 seconds, default is 60.0 seconds
def expensive_operation(a, b):
    ...
    ...

```
