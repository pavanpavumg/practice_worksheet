n = 13,30,45,78,20,100
S_largest = 0
largest = n[0]
for nums in n:
    if nums>largest:
        S_largest = largest
        largest = nums
    elif nums>S_largest and nums<largest:
        S_largest = nums
print(S_largest)



