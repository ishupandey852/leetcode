class Solution:
    def maximumProduct(self, nums):
        # Find the 3 largest and 2 smallest numbers
        # Sorting takes O(N log N) time
        nums.sort()
        
        option1 = nums[-1] * nums[-2] * nums[-3]
        
        option2 = nums[0] * nums[1] * nums[-1]
        
        return max(option1, option2)