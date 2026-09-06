class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If s is shorter than t, it can't contain t as a subsequence
        if m < n:
            return 0
            
        # 1D DP table representing the current row dp[j] for t[:j]
        # Initialize dp[0] = 1 (empty string t can be formed 1 way)
        dp = [1] + [0] * n
        
        for char_s in s:
            # Iterate backwards to avoid using updated values from the same s character
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]