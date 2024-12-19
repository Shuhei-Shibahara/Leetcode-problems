class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for c in magazine:
            count[c] = 1 + count.get(c,0)

        for l in ransomNote:
            if l not in count or count[l] <= 0:
                return False
            count[l] -= 1

        
        return True