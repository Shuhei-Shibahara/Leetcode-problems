class Solution:
    #compare strings to each other with index
    #when you find the a letter thats out of place then return that string
    def longestCommonPrefix(self, strs: List[str]) -> str:

        check = strs[0]
        for i in range(len(check)):
            for word in strs[1:]:
                if i == len(word) or check[i] != word[i]:
                    return word[0:i]
        return check
        
