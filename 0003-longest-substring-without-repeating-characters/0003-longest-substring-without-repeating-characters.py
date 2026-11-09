class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = best = 0
        for right, ch in enumerate(s):
            if seen.get(ch, -1) >= left:
                left = seen[ch] + 1
            seen[ch] = right
            best = max(best, right - left + 1)
        return best