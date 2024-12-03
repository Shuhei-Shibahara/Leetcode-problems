class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #compare 2 words
        #if its not the prefix or if its longer then False
        lex = {c : i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if lex[w1[j]] > lex[w2[j]]:

                        return False
                    break
        
        return True
