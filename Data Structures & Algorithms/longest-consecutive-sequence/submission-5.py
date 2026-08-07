class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        max_result = 1
        result=1
        if nums == []: return 0
        for s in sequence:
            if s-1 not in sequence:
                result = 1
                continue
            result+=1
            max_result = max(max_result, result)
        return max_result

