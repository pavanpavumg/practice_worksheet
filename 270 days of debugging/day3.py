class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_length = 0

        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))