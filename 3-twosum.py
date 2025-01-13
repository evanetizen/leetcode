from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_tracker = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_tracker:
                return [num_tracker[diff], idx]
            num_tracker[num] = idx
        return []
