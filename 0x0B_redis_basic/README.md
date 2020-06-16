# 0x0B. Redis basic
## Learning Objectives
   - Learn how to use redis for basic operations
   - Learn how to use redis as a simple cache

## Tasks
### [0. Writing strings to Redis](./exercise.py)
Create a Cache class. In the `__init__` method, store an instance of the Redis client as a private variable named _redis and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.

### [1. Reading from Redis and recovering original type](./exercise.py)
Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.

In this exercise we will create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

Remember to conserve the original Redis.get behavior if the key does not exist.

The following code should not raise:
```
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

As a bonus, you can implement the get_str and get_int methods that will automatically parametrize Cache.get with the correct conversion function.