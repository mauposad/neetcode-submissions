class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        
        result = 1
        for s in sequence:
            if s-1 not in sequence:
                continue
            result+=1
        return result

