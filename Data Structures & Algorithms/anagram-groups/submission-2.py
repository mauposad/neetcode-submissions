class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #hashmap of solutions

        for s in strs: # for loop to traverse strs
            count = [0] * 26 #array for key value for hash map
            for c in s: #traversing each letter in word for key
                count[ord(c)-ord("a")]+=1 #calculating key by using ascii values 
            result[tuple(count)].append(s)# setting value of key to the instance of word
        return list(result.values()) # win condition