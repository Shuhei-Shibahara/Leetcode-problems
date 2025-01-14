class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start,end = s.split(":")
        s_col, s_row = start[0], int(start[1])
        e_col, e_row = end[0], int(end[1])
        result = []
        for i in range(ord(s_col), ord(e_col) + 1):
            for j in range(s_row, e_row + 1):
                result.append(f"{chr(i)}{j}")
        return result
        