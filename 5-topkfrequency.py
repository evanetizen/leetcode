class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = defaultdict(list)
        for key, value in counts.items():
            buckets[value].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for element in buckets[i]:
                res.append(element)
                if len(res) == k:
                    return res


# next time try to do bucket sort with a list!
