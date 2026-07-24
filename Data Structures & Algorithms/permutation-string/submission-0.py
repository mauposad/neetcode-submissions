class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] +=1
            s2Count[ord(s2[i]) - ord('a')] +=1
            """ hash map at index in a-z incremented by 1 if present"""
        
        match = 0
        for i in range(26): # initialize match score
            match += (1 if s1Count[i] == s2Count[i] else 0 )
        
        l = 0
        for r in range(len(s1), len(s2)):
            if match ==26:
                return True

            #updating hashmap of s2Count for right pointer
            index = ord(s2[r]) - ord('a') # index in a-z of r pointer
            s2Count[index]+=1
            if s1Count[index] == s2Count[index]: 
                match+=1 # index is now equal
            elif s1Count[index]+1 == s2Count[index]:
                match-=1 # index was made too large
            
            #updating hash map of s2Count for left pointer
            index = ord(s2[l]) - ord('a')# index in a-z of left pointer
            s2Count[index]-=1
            if s1Count[index] == s2Count[index]:
                match+=1 # index is equal
            elif s1Count[index]-1 == s2Count[index]:
                match-=1 # index was made too small
            l+=1

        return match == 26

        


