
def binary_search(arr: list[int], k: int) -> int:
    if len(arr) == 0:
        return -1
    def binary_search_helper(start: int, end: int) -> int:
        if start > end:
            return -1
        if start == end:
            if arr[start] == k:
                return start
            return -1
        mid = start + (end - start) // 2
        if arr[mid] == k:
            return mid
        elif k < arr[mid]:
            return binary_search_helper(start, mid - 1)
        return binary_search_helper(mid+1, end)
    return binary_search_helper(0, len(arr)-1)

def search_in_rotated(arr: list[int], k: int) -> int:
    if len(arr) == 0:
        return -1
    def find_rotated_helper(start: int, end: int) -> int:
        if start > end:
            return -1
        if start == end:
            if arr[start] == k:
                return start
            return -1
        mid = start + (end - start) // 2
        if arr[mid] == k:
            return mid

        if arr[start] <= arr[mid]:
            if arr[start] <= k < arr[mid]:
                return binary_search_helper(start, mid - 1)
            else:
                return find_rotated_helper(mid + 1, end)
        else:
            if arr[mid] < k <= arr[end]:
                return binary_search_helper(mid + 1, end)
            else:
                return find_rotated_helper(start, mid - 1)
    def binary_search_helper(start: int, end: int) -> int:
        if start > end:
            return -1
        if start == end:
            if arr[start] == k:
                return start
            return -1
        mid = start + (end - start) // 2
        if arr[mid] == k:
            return mid
        elif k < arr[mid]:
            return binary_search_helper(start, mid - 1)
        return binary_search_helper(mid+1, end)
    return find_rotated_helper(0, len(arr) - 1)

assert search_in_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search_in_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_in_rotated([4, 5, 6, 7, 0, 1, 2], 4) == 0

assert binary_search([1, 2, 3, 4, 5], 3) == 2
assert binary_search([1, 2, 3, 4, 5], 1) == 0
assert binary_search([1, 2, 3, 4, 5], 5) == 4

class TreeNode:
    def __init__(self, val: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

def left_tree_view(root: TreeNode) -> list[int]:
    res: list[int] = []
    helper_q: list[TreeNode] = [root]
    while len(helper_q) > 0:
        curr = helper_q.pop(0)
        level_len: int = len(helper_q)
        if curr.left:
            helper_q.append(curr.left)
        if curr.right:
            helper_q.append(curr.right)
        res.append(curr.val)
        for _ in range(level_len):
            level_curr = helper_q.pop(0)
            if level_curr.left:
                helper_q.append(level_curr.left)
            if level_curr.right:
                helper_q.append(level_curr.right)
    return res