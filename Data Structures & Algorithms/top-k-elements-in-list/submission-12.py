from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums)+1)]
        result = []

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for num, count in counts.items():
            buckets[count].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for i, num in count.items():
            freq[num].append(i)

        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res





