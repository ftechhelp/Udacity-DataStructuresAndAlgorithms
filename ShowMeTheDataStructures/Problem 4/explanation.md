## Reasoning Behind Decisions:
I used recursion to solve this issue since it basically acts as a stack, so it's easier to read and makes the function much simpler. \
This uses a depth first search approach to find the user. The downside of this function is it could potentially hit a stack overflow because of recursion. \
You could potentially add a depth limit to groups or use a list that acts as a stack instead of recursion. You could also optimize the Group class by using \
a set or hash table for user lookup.


## Time Efficiency:
The worst-case time complexity for the is_user_in_group function is O(n), where n is the total number of groups and subgroups.

## Space Efficiency:
The worst-case space complexity for the is_user_in_group function is O(n), where n is the maximum depth of the group hierarchy.
