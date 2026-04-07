def string_reverse(srt):
    left = 0
    right = len(str) - 1
    while left <= right:
        temp = left
        left = right
        right = temp
        left+=1
        right-=1
    return "" .join(str)
str = 'pavan'
string_reverse(str)
print(string_reverse(str))