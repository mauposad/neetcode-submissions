class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #not the fastest time complexity. How can it be made faster? 
        # Better way to sort this? or different structure that number of computations?
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
