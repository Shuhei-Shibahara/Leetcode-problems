class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        i = 0

        while k:
            digit = k % 10 #this is getting the most right number in k

            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)
            
            carry = num[i] // 10 #this is making it so we get the remainder
            num[i] = num[i] % 10 #this is making it so if 2 % 10 = 2
            k = k // 10
            k += carry
            i += 1
        
        num.reverse()
        return num
