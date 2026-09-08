class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
            
        # For n <= 10^5, all numbers >= 1000 have exactly 1 comma
        return n - 1000 + 1
        