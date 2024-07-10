# importing libraries
import time
import math

def make_key(args, kwds, typed):
    key = args
    if kwds:
        key += (object(),)
        for item in kwds.items():
            key += item
    if typed:
        key += tuple(type(arg) for arg in args)
        if kwds:
            key += tuple(type(arg) for arg in kwds.values())
    return key

# decorator to calculate duration
# taken by any function.
def lru_cache(user_function):
    
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    sentinel = object()      # unique object used to signal cache misses
    cache = {}                                # RESULTS SAVES HERE
    cache_get = cache.get    # bound method to lookup a key or return None

    def wrapper(*args, **kwds):
        hits, misses = 0, 0
        # Simple caching without ordering or size limit
        key = make_key(args, kwds,True)     # BUILD A KEY FROM ARGUMENTS
        print(key)
        result = cache_get(key, sentinel)     # TRYING TO GET PREVIOUS CALLS RESULT
        if result is not sentinel:            # ALREADY CALLED WITH PASSED ARGS
            hits += 1
            return result                     # RETURN SAVED RESULT
                                              # WITHOUT ACTUALLY CALLING FUNCTION
        misses += 1
        result = user_function(*args, **kwds) # FUNCTION CALL - if cache[key] empty
        cache[key] = result                   # SAVE RESULT
        return result
    return wrapper



# this can be added to any function present,
# in this case to calculate a factorial
@lru_cache
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    print(math.factorial(num))

# calling the function.
factorial(10)