class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)
                
nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))

        

    
         