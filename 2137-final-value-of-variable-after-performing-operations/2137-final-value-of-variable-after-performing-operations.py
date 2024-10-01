class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0
        for i in operations:
            if i == "X--" or i == "--X":
                total -= 1
            elif i == "X++" or i =="++X":
                total += 1
            else:
                total += 0
        
        return total
