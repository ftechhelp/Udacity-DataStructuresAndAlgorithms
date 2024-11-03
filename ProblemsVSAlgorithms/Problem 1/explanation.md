
## Reasoning Behind Decisions:
I used a binary search to find the square root of a number instead of just iterating over every number below the given number. \
This approach drastically reduces the amount of checks we had to do.

## Time Efficiency:
Doing a binary search is O(log n) complexity

## Space Efficiency:
The solution uses a constant amount of space only to store variables left, right and middle, regardless of the number, meaning it's O(1) complexity