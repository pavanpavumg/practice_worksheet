from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarysearch(nums, target, left_search):
            left = 0
            right = len(nums) - 1
            i = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    i = mid
                    if left_search:
                        right = mid - 1
                    else:
                        left = mid + 1

            return i

        left = binarysearch(nums, target, True)
        right = binarysearch(nums, target, False)

        return [left, right]
sort = Solution()
nums = [5,7,7,8,8,10] 
target = 8

print(sort.searchRange(nums, target))
