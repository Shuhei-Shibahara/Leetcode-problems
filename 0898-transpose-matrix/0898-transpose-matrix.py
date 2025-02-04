class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        res = []

        for i in range(col):
            add = []
            for j in range(row):
                add.append(matrix[j][i])
            
            res.append(add)
        
        return res
