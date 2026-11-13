from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            hm[n] = i
        
        for key, value in hm.items():
            diff = target - value
            if diff in hm and hm[diff]!= i:
                return [key, hm[diff]]
        return []
        
        