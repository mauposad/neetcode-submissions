class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result=0

        """valid window = window_length - count of most frequent character"""
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0) # adding into hashmap

            if right - left + 1 - max(count.values()) > k: #checking if window valid
                count[s[left]]-=1
                left+=1

            result = max(result, right - left + 1) # updating max frequency
            # only need window size since we confirmed window size was valid in previous step

        return result

