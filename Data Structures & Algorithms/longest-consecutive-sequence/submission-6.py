class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        max_result = 0
        result=0
        if nums == []: return 0
        
        for s in nums:
            if s-1 not in sequence:
                result = 0
                while s+result in sequence:
                    result+=1
                    max_result = max(max_result, result)
        return max_result

