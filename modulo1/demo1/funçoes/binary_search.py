
nums = [1, 3, 5, 7, 9, 11, 13]
target = 7
target = 6

def binary_search(nums, target):
    target = 6
    mid = len(nums) // 2
    if nums[mid] == target:
        return True
    if nums[mid] > target:
        (nums[:mid],target)
    else:
        (nums[mid+1:], target)
    return False
print(binary_search(nums,target))


