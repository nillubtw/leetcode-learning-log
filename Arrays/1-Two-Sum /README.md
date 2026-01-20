# 1. Two Sum

🔗 LeetCode: https://leetcode.com/problems/two-sum/

## Learning Log
This was my first approach to the problem. I used a simple brute-force method
by checking all possible pairs of numbers until I found the one that matched
the target.

While this solution works, it is not optimal and helped me understand why
better approaches are needed for larger inputs.

## Approach
- Use two nested loops
- Check every unique pair
- Return indices when the target sum is found

## Complexity
- Time complexity: O(n²)
- Space complexity: O(1)
