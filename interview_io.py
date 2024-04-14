"""
Given an array (sorted), return the count of a particular tagerget element
arr: [1,2,2,3,3,3,3,4]

findCount(arr, 2) = 2
findCount(arr, 3) = 4
findCount(arr, 5) = 0
"""

# def insert_at(nums, target):
#     left = 0
#     right = len(nums) - 1
#     mid = (left + right) // 2
#     while left < right:
#         if nums[mid] == target:
#             return mid
#         if nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#         mid = (left + right) // 2
#     return left


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    # if target in nums:
    #     return nums.index(target)
    # else:
    #     if nums[-1] < target:
    #         return len(nums)

    #     greater_nums = list(filter(lambda x: x > target, nums))
    #     return nums.index(greater_nums[0])

    # =============================
    # binary search way

    # if nums[0] >= target:
    #     return 0
    left_pointer = 0
    right_pointer = len(nums)

    mid = (left_pointer + right_pointer) // 2  # // does the floor- integer division

    # nums = [2, 7, 8, 10]
    # target = 9
    # left = 0
    # right= 3
    # mid = 1
    # [1]
    while left_pointer < mid:  # left_pointer = right_pointer -1; mid = left_pointer
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            # left = 2
            left_pointer = mid + 1  # potentially this was right_pointer!
        else:
            right_pointer = mid  # suppose left_pointer was mid - 1
        # mid = (3 + 2) // 2 = 2
        mid = (right_pointer + left_pointer) // 2  # always get 0
    return left_pointer


nums = [0, 1, 2, 3, 4, 5]
searchInsert(nums, 5)
searchInsert(nums, 0)
searchInsert(nums, 2)
searchInsert(nums, 6)
searchInsert(nums, 10)
searchInsert(nums, -1)
