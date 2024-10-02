## Reasoning Behind Decisions:
Used an OrderedList to keep the chain to be able to efficiently find a block by using the hash and having the option of getting it by it's index. \
I could of potentially of had 2 dictionaries for better efficiency when getting a block by index, but I decided on an OrderedList instead for readability.

## Time Efficiency:
The worst-case time complexity for the blockchain implementation is O(n), where n is the number of blocks.

## Space Efficiency:
The worst-case space complexity for the blockchain implementation is O(n), where n is the number of blocks.
