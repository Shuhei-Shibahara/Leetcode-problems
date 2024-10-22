class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checker = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                checker.remove(nums[L])
                L += 1

            if nums[R] in checker:
                return True
            checker.add(nums[R])
        return False