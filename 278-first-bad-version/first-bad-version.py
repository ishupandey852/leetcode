# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # mid could be the first bad version, so keep it in search space
                right = mid
            else:
                # mid is good, so the first bad version must be after mid
                left = mid + 1
                
        return left