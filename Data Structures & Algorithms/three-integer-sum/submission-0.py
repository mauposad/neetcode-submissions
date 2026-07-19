class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort for two sum II
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # check for duplicates
                continue
            l, r = i+1, (len(nums)-1)

            while l < r: # two sum II
                three_sum = a + nums[l]+nums[r]
                if three_sum > 0:
                    r-=1
                elif three_sum < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        """additional duplicate check for two sum II"""
                        l+=1
                
        return res
