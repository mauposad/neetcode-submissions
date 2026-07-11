class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums: # filling hash map with count
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items(): #2d array used for bucket sort
            freq[c].append(n)

        res = [] #answer array
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        

        