from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(int)

        for i in range(len(nums)):
            hm[i] = nums[i]
        
        for key, value in hm.items():
            print(f"key: {key}, value {value}")
        
        