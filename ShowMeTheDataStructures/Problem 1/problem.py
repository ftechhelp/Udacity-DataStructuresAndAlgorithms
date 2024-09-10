from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity = 5):

        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int | str):
        
        retrieved_item = self.cache[key] if key in self.cache else -1

        if retrieved_item == -1:
            return retrieved_item
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: int | str, value):
        
        self.__handle_at_capacity()

        if key == None or key == "":
            return -1

        self.cache[key] = value

    def print(self):
        print(self.cache)
        return 

    def __handle_at_capacity(self):

        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

# Test Case 1: Basic functionality
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
assert our_cache.get(1) == 1   # Returns 1
assert our_cache.get(2) == 2   # Returns 2
assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)  # This should evict key 3
assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

# Test Case 2: Nulls and Empties
our_cache.set(7, None) #This should evict key 4
assert our_cache.set(None, 7) == -1 #Return -1 because you need a valid key
assert our_cache.set("", "7") == -1 #Return -1 because you need a valid key
assert our_cache.get(None) == -1 #This should return -1 since it was never set
assert our_cache.get("") == -1 #This should return -1 since it was never set
assert our_cache.get(7) == None #Returns None
assert our_cache.get(4) == -1 #Returns -1, 4 was evicted

# Test Case 3: Big Keys and different types of values
our_cache.set(848578943579347, "jfhjfhkjfhjkfhsdkjgfhjkghfdjkghjkhdfkjshagdshjfghjds")
our_cache.set(7.35, "")
our_cache.set(0, 85784574389753894759384)
our_cache.set("ndfhbdsf8gdf78sg83b4b34k5bfhsd789fgh97834", [1, 2, 3, 4, 5, 6, 7])
our_cache.set("woo", 35456.9384756)
#only thing in the cache now should be items from test case 3
assert our_cache.get(7) == -1 #Return -1, 7 should be evicted
assert our_cache.get(848578943579347) == "jfhjfhkjfhjkfhsdkjgfhjkghfdjkghjkhdfkjshagdshjfghjds" #Returns long-ish string
assert our_cache.get(7.35) == "" #Returns blank
assert our_cache.get(0) == 85784574389753894759384 #Returns big int
assert our_cache.get("ndfhbdsf8gdf78sg83b4b34k5bfhsd789fgh97834") == [1, 2, 3, 4, 5, 6, 7] #Returns list
assert our_cache.get("woo") == 35456.9384756 #Returns decimal point number