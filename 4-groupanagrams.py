from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord("a")] += 1
            result[tuple(char_count)].append(s)

        return result.values()
