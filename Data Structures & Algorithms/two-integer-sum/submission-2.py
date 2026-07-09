class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force two sum
        total = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                total = nums[i] + nums[j]
                if total == target:
                    return [i,j]
