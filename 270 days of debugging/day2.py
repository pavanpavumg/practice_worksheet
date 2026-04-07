class Solution:
    def compress(self, chars):
        i = 0          # read pointer
        write = 0      # write pointer

        while i < len(chars):
            char = chars[i]
            count = 0

            # count same characters
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1 

            # write the character
            chars[write] = char
            write += 1

            # write count if > 1
            if count > 1:

                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
chars = ["a","a","b","b","c","c","c"]
sol = Solution()
print(sol.compress(chars))