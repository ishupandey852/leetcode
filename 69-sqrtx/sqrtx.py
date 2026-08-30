class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left, right = 1, x // 2
        ans = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if mid * mid <= x:
                ans = mid        # mid is a valid candidate, store it
                left = mid + 1   # Try searching for a larger valid integer
            else:
                right = mid - 1  # mid * mid is too large, search lower
                
        return ans