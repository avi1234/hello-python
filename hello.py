def binary_search(nums: list[int], target: int) -> int:
    """Return the index of target in a sorted array, or -1 if absent."""
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

data: list[int] = [1, 3, 5, 7, 9, 11]
for value in (3, 4, 11):
    result = binary_search(data, value)
    print(f"{value} -> {result}")