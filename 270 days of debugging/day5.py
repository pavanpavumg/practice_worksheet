# class Solution:
#     def maxOperations(self, nums, k):
#         nums.sort()
#         left, right = 0, len(nums) - 1
#         count = 0

#         while left < right:
#             s = nums[left] + nums[right]

#             if s == k:
#                 count += 1
#                 left += 1
#                 right -= 1
#             elif s < k:
#                 left += 1
#             else:
#                 right -= 1

#         return count

# nums = [1,2,3,4]
# k = 5
# sol = Solution()
# print(sol.maxOperations(nums, k))


nums = [10, 20, 30,40,]
nums.remove(20)
nums.pop(1)
print(nums)