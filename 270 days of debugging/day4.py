class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import defaultdict
        
        groups = defaultdict(list)

        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            
            length = j - i
            groups[s[i]].append(length)
            i = j

        ans = -1

        for char in groups:
            lengths = groups[char]
            lengths.sort(reverse=True)

            for k in range(len(lengths)):
                L = lengths[k]

                for x in range(1, L + 1):
                    total = 0
                    for l in lengths:
                        if l >= x:
                            total += l - x + 1
                    
                    if total >= 3:
                        ans = max(ans, x)

        return ans


s = "aaabaaa"
sol = Solution()
print(sol.maximumLength(s))