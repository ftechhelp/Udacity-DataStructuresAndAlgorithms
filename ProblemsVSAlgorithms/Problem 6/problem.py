def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """

    minimum = None
    maximum = None

    for integer in ints:

        if minimum == None:
            minimum = integer

        if maximum == None:
            maximum = integer

        if integer < minimum:
            minimum = integer

        if integer > maximum:
            maximum = integer

    return (minimum, maximum)


### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")