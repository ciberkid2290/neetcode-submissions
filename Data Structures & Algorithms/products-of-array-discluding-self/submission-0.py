class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        total_product = 1
        for n in nums:
            if n:
                total_product *= n
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            res = []
            for n in nums:
                res.append(0)
            return res

        res = [0] * len(nums)
        for ind, val in enumerate(nums):
            if zero_cnt:
                if val:
                    res[ind] = 0
                else:
                    res[ind] = total_product
            else:
                res[ind] = total_product // val
        return res