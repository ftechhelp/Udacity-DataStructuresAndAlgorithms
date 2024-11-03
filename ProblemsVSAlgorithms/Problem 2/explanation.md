
## Reasoning Behind Decisions:
Used a modified version of a binary search. Since we know that one side will be sorted, we use that information to find which half the number belongs too and then keep repeating the process until the number is found.

## Time Efficiency:
Doing a binary search is O(log n) complexity

## Space Efficiency:
The solution uses a constant amount of space only to store variables left, right and middle, regardless of the number, meaning it's O(1) complexity