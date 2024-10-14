class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        table = {}

        # Build the table
        for i, size in enumerate(groupSizes):
            if size not in table:
                table[size] = [i]
            else:
                table[size].append(i)

        return self.create_table(table)

    def create_table(self, table):
        result = []
        for size, indices in table.items():
            print(size, indices)
            for i in range(0, len(indices), size):
                result.append(indices[i:i + size])
        
        return result