def nearest_value(nums, target):
    if len(nums) == 0: return 'Error'
    nums= list(nums)
    distances_to_target = []
    for num in nums:
        distances_to_target.append(abs(target - num))
    return nums[distances_to_target.index(min(distances_to_target))]

print(nearest_value({4, 7, 10, 11, 12, 17}, 9))