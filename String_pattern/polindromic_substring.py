class Solution:
    @staticmethod
    def countSubstrings(s: str) -> int:
        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count+=1
                left-=1
                right+=1
            return  count

        result = 0


        for i in range(len(s)):
            result+=expand(i,i)
            result+=expand(i, i+1)

        return result
s = "aaa"
polindromic = Solution.countSubstrings(s)
print(polindromic)      

        

        