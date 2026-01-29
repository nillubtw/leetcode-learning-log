# 3. Longest Substring Without Repeating Characters

🔗 LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Learning Log
This problem introduced the sliding window technique. The key idea was to
maintain a window of unique characters and dynamically adjust it when a
duplicate character was encountered.

Understanding how to move the left pointer only when needed helped optimize
the solution to linear time.

## Approach
- Use a sliding window with two pointers (`left` and `right`)
- Maintain a set to track unique characters in the current window
- When a duplicate character is found, shrink the window from the left
- Update the maximum length during each valid window

## Complexity
- Time complexity: O(n)
- Space complexity: O(min(n, k))  
  where `k` is the character set size
