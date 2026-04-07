class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ""

        for i in range(len(s)):
            add1 = expand(i, i)       # odd
            add2 = expand(i, i+1)     # even

            if len(add1) > len(result):
                result = add1

            if len(add2) > len(result):
                result = add2

        return result



s = "babad"
longest = Solution().longestPalindrome(s)
print(longest)