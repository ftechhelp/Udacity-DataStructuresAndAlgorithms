
## Reasoning Behind Decisions:
I used mergesort to sort the digits in decending order and then alternated between each digit, assigning it to one number or the other to make up the two numbers that can maximize the sum. \
To handle negative numbers, I made sure to put all the positive numbers together in one number and all the negative numbers together in the other. The only downside to this method is it breaks the \
"both the numbers cannot differ by more than 1" rule, but it stays true to having the maximum sum, assuming you can only concatenate digits together and can't actually do math, which is what I understood from the examples.

## Time Efficiency:
The worst-case time complexity of the solution is O(n log(n)) due to the merge sort I used.

## Space Efficiency:
The worst-case space complexity of the solution is O(n log(n)) due to the recursive mergesort.