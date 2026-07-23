class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes (e.g., -121 != 121-)
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
            
        # When length is odd, we can get rid of the middle digit by reverted_number // 10
        # e.g. for 12321, at the end of loop x = 12, reverted_number = 123, so x == reverted_number // 10
        return x == reverted_number or x == reverted_number // 10