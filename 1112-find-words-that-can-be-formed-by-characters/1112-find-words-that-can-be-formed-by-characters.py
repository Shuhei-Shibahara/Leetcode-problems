class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for word in words:
            test = defaultdict(int)
            good = True
            for c in word:
                test[c] += 1
                if c not in count or test[c] > count[c]:
                    good = False
                    break
                
            if good:
                res += len(word)
        
        return res
