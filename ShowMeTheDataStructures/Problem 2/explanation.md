
## Reasoning Behind Decisions:
Using a recursive method, we go through each file in each folder only once and store the file paths that match the suffix provided in a list. \
We explore the directory in a depth first manner exploring each directory to it's fullest depth before backtracking. \
Using recursion breaks down the problem into smaller, more managable pieces.


## Time Efficiency:
The worst-case time complexity of the find_files function is O(n), where n is the total number of files and subdirectories in the directory tree.

## Space Efficiency:
The worst-case space complexity of the find_files function is O(n), where n is the total number of files in the directory tree.
