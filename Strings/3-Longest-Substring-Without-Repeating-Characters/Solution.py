class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Use sliding window technique
        characters = set()
        left=0 #Left pointer starting at index 0
        max_len=0 # length of longest string

        for right in range(len(s)): #right pointer
            while s[right] in characters: #duplicate character found
                characters.remove(s[left]) 
                left+=1 #move the left pointer forward
            characters.add(s[right])
            max_len= max(max_len, right-left+1) #comparing longest of max_len and lenght of current string
        return max_len





        

        
