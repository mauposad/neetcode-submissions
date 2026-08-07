class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left, right = 0, len(nums)-1
        while left < right:
            if left == right:
                return True
            left+=1
            right-=1

        return False
