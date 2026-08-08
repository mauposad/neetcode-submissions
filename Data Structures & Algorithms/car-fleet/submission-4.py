class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_arr = []
        for i in range(len(position)):
            combined_arr.append((position[i], speed[i]))
        
        combined_arr.sort(reverse = True)
        
        stack = []
        for item in combined_arr:
            curr_time = (target - item[0]) / item[1]
            stack.append(curr_time)
            if len(stack) > 1 and curr_time <= stack[-2]:
                stack.pop()

        return len(stack)