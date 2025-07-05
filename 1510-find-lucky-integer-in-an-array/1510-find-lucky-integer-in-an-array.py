from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        lucky = -1
        for num, freq in count.items():
            if num == freq:
                lucky = max(lucky, num)
        return lucky

