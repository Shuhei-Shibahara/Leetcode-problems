class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        merged = []

        while word1 and word2:
            merged.append(word1.pop(0))
            merged.append(word2.pop(0))
        
        if word1:
            merged = merged + word1
        
        if word2:
            merged = merged + word2

        
        return ''.join(merged)