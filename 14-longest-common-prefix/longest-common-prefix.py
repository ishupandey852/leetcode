class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        prefix = []
        # Zip characters at the same index across all strings
        for chars in zip(*strs):
            # Check if all characters at the current position are identical
            if len(set(chars)) == 1:
                prefix.append(chars[0])
            else:
                break
                
        return "".join(prefix)