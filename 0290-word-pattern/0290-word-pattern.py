class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #label each latter to a word
        #going through the set that you created if it doesnt match then return False
        chartoword = {}
        wordtochar = {}
        s = s.split(' ')

        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if pattern[i] in chartoword and chartoword[pattern[i]] != s[i]:
                return False
            if s[i] in wordtochar and wordtochar[s[i]] != pattern[i]:
                return False
            chartoword[pattern[i]] = s[i]
            wordtochar[s[i]] = pattern[i] 
        
        return True
            
    
        
        return True
