class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        maxFreq = max(freq.values())
        
        buckets = [[] for _ in range(maxFreq + 1)]
        for nums, count in freq.items():
            buckets[count].append(nums)
        
        res = []
        for i in range(maxFreq, 0, -1):
            buckets[i].sort(reverse=True)

            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res