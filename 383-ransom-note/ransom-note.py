from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        note_counts = Counter(ransomNote)
        mag_counts = Counter(magazine)
        
        for char, count in note_counts.items():
            if mag_counts[char] < count:
                return False
                
        return True