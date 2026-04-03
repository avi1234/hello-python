def binary_search(arr: list[int], val: int) -> int:
    """search val in array, return -1 if not exists"""
    if len(arr) == 0:
        return -1
    
    start:int = 0
    end: int = len(arr)-1

    while(start <= end):
        mid_index = start + (end - start) // 2
        if val == arr[mid_index]:
            return mid_index
        elif val < arr[mid_index]:
            end = mid_index-1
        else:
            start = mid_index+1
    
    return -1

def binary_search_recursion(arr: list[int], val: int, start: int, end: int) -> int:
    if len(arr) == 0 or end < start:
        return -1
    mid_index = start + (end - start) // 2
    if arr[mid_index] == val:
        return mid_index
    if val < arr[mid_index]:
        return binary_search_recursion(arr, val, start, mid_index - 1)
    return binary_search_recursion(arr, val, mid_index + 1, end)

assert binary_search([1,3,5,7],3) == 1
assert binary_search([],3) == -1
assert binary_search([3],3) == 0
assert binary_search([1,3,5,7],9) == -1
assert binary_search([1,3,5,7,9,11],9) == 4
assert binary_search([1,3,5,7,9,11],11) == 5

assert binary_search_recursion([1,3,5,7],3, 0, 3) == 1
assert binary_search_recursion([],3, 0, 0) == -1
assert binary_search_recursion([3],3, 0, 1) == 0
assert binary_search_recursion([1,3,5,7],9, 0, 3) == -1
assert binary_search_recursion([1,3,5,7,9,11],9, 0, 5) == 4
assert binary_search_recursion([1,3,5,7,9,11],11, 0, 5) == 5

class TreeNode:
    def __init__(self, val: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: TreeNode | None) -> str:
    if root is None:
        return ""
    root_as_arr: list[int] = []
    def helperDFS(node: TreeNode | None) -> None:
        if node is None:
            return
        helperDFS(node.left)
        root_as_arr.append(node.val)
        helperDFS(node.right)
    helperDFS(root)
    return str(root_as_arr)

print(serialize(TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6))))

def longest_subarray_length(arr:list[int], k:int) -> int:
    if len(arr) == 0:
        return 0
    helper_dict:dict[int, int] = {0: -1}
    max_length:int = 0
    prefix_sum:int = 0
    for i, val in enumerate(arr):
        prefix_sum += val
        helper_val = helper_dict.get(prefix_sum-k)
        if helper_val is not None and max_length < i - helper_val:
            max_length = i - helper_val
        if helper_dict.get(prefix_sum) is None:
            helper_dict[prefix_sum] = i
    return max_length

def longest_subarray_divided(arr:list[int], k:int) -> int:
    if len(arr) == 0 or k <=0:
        return 0
    helper_dict:dict[int, int] = {0: -1}
    max_length:int = 0
    prefix_sum:int = 0
    for i, val in enumerate(arr):
        prefix_sum += val
        helper_val = helper_dict.get(prefix_sum%k)
        if helper_val is not None and max_length < i - helper_val:
            max_length = i - helper_val
        if helper_dict.get(prefix_sum%k) is None:
            helper_dict[prefix_sum%k] = i
    return max_length

def count_subarrays_with_sum(arr: list[int], k: int) -> int:
    if len(arr) == 0:
        return 0
    prefix_sum = 0
    prefix_counts: dict[int, int] = {0: 1}
    total = 0
    for val in arr:
        prefix_sum += val
        total += prefix_counts.get(prefix_sum - k, 0)
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
    return total

def count_subarrays_with_sum2(arr: list[int], k: int) -> int:
    if len(arr) == 0:
        return 0
    helper_dict: dict[int, int] = {0: 1}
    res: int = 0
    prefix_sum: int = 0
    for val in arr:
        prefix_sum += val
        check_key = helper_dict.get(prefix_sum - k)
        if check_key is not None:
            res += check_key
        helper_dict[prefix_sum] = helper_dict.get(prefix_sum, 0) + 1
    return res

def max_length_binary(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    helper_dict: dict[int, int] = {0: -1}
    max_length:int = 0
    prefix_sum: int = 0
    for i, val in enumerate(arr):
        prefix_sum += (val+1)
        if prefix_sum%3 == 0 and helper_dict.get(prefix_sum%3):
            max_length = max(max_length, i - helper_dict[prefix_sum%3])
        if helper_dict.get(prefix_sum) is None:
            helper_dict[prefix_sum] = i 
    return max_length

assert max_length_binary([]) == 0
assert max_length_binary([0, 1]) == 2
assert max_length_binary([0, 1, 0]) == 2
assert max_length_binary([0, 0, 1, 0, 1, 1, 0]) == 6
assert max_length_binary([1, 1, 1, 0, 0, 0, 1, 0]) == 8



assert longest_subarray_length([], 0) == 0          # empty input
assert longest_subarray_length([5, -5], 0) == 2     # whole array zero-sum
assert longest_subarray_length([2, -1, 2, -1, 2], 3) == 3
assert longest_subarray_length([3, 4, -7, 5, -6, 6], 5) == 6
assert longest_subarray_length([-2, -1, 2, 1], 0) == 4
