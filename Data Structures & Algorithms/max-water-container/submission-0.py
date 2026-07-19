class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_cap = 0
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            cap = w * h
            max_cap = max(max_cap, cap)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return max_cap

