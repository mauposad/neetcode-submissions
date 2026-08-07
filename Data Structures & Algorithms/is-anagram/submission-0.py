class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1= set(s)
        set2= set(t)
        if set1 == set2:
            return True
        return False