class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        prev_num = None
        total = 0
        for i in s:
            if prev_num:
                if roman[prev_num] < roman[i]:
                    total += roman[i] - roman[prev_num]*2
                else:
                    total += roman[i]
            else:
                total += roman[i]
            prev_num = i
        
        return total
        
