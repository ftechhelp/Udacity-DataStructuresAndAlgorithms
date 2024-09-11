
## Reasoning Behind Decisions:
I used an OrderedDict for the cache to give me the ability to store information without having to iterate through the list to find the value. \
The fact that an OrderedDict keeps note of the position facilitates being able to move the data to the end of the list to keep the order of the least recently used. \
If the cache becomes full, you can easily pop the first item from the dictionary before adding the new value. Since we add new values to the end and move values that have been fetched to the end as they are being fetched, \
we know that the first item in the list is the least recently used (fetched or inserted).

## Time Efficiency:
The worst-case time complexity is O(1) since we are using a dictionary to set and get data which involve constant time operations.

## Space Efficiency:
The worst-case space complexity is O(n), where n is the capacity of the cache. \
The space complexity is determined by the capacity of the cache, not by the size of the input data.