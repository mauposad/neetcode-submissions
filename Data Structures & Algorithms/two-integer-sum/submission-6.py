class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hm and hm[complement] != i :
                return [i, hm[complement]]