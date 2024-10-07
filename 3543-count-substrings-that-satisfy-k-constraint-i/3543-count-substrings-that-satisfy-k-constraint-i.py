class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        #we must count all the substring possible that has the k-constraint
        #use sliding window method
        #we will keep moving the window over making sure there isnt breaking the constraint

        length = len(s)
        total = 0

        for i in range(length):
            zero_count, one_count = 0,0
            for j in range(i,length):
                if s[j] == '0':
                    zero_count += 1
                else:
                    one_count += 1
                
                if zero_count <= k or one_count <= k:
                    total += 1
        
        return total
