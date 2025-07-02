from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        total = 0
        current = 0
        
        for i in range(2, len(nums)):
           
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current += 1
                total += current
            else:
                current = 0
        
        return total
