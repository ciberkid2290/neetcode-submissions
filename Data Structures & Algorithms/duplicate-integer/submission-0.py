class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenMap = {}

        for i, num in enumerate(nums):
            if num in seenMap:
                return True
            seenMap[num] = i
        return False