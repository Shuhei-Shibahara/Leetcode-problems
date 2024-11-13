class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        curr = 0
        l,r = 1, 2**(n-1)

        for _ in range(n-1):
            mid = (r+l) // 2

            if mid < k:
                l = mid + 1
                curr = 0 if curr else 1
            else:
                r = mid


        return curr
        # stack = [[0]]
        # times = n - 1
        # while times:
        #     curr = stack[-1]
        #     add = []
        #     for j in curr:
        #         if j == 0:
        #             add.append(0)
        #             add.append(1)
        #         else:
        #             add.append(1)
        #             add.append(0)
        #     stack.append(add)
        #     times -= 1
        
        # return stack[n-1][k-1]
