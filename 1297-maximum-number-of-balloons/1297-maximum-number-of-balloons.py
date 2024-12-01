class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #lets count the number of letters in text
        #count the letter in balloons
        #if we find the min number between the divided 2 it should be the res

        t = Counter(text)
        balloon = Counter('balloon')
        res = len(text)

        for c in balloon:
            res = min(res, t[c]//balloon[c])
        
        return res