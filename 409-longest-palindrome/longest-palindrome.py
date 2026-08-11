class Solution:
    def longestPalindrome(self, s):
        unpaired = set()
        length = 0
        
        for char in s:
            if char in unpaired:
                unpaired.remove(char)
                length += 2  # Found a pair
            else:
                unpaired.add(char)
                
        # If there are left over unpaired characters, put one in the center
        if unpaired:
            length += 1
            
        return length
        