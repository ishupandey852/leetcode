class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # 1. Precompute suffix minimums: suffix_min[i] = min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        # 2. Iterate from left to right maintaining prefix maximum
        prefix_max = float('-inf')
        
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            instability_score = prefix_max - suffix_min[i]
            
            if instability_score <= k:
                return i
                
        return -1
        