
class TreeNode:
    def __init__(self, val: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode | None) -> bool:
    if root is None:
        return True
    def validate(node: TreeNode | None, min: int, max: int) -> bool:
        if node is None:
            return True
        if node.val <= min or node.val >= max:
            return False
        return validate(node.left, min, node.val) and validate(node.right, node.val, max)
    return validate(root, float('-inf'), float('inf'))

def kth_smallest(root: TreeNode | None, k: int) -> TreeNode | None:
    if root is None or k < 1:
        return None
    visited_nodes: int = 0
    def dfs_helper(node: TreeNode | None) -> TreeNode | None:
        nonlocal visited_nodes
        if node is None:
            return None
        dfs_res = dfs_helper(node.left)
        if dfs_res:
            return dfs_res
        visited_nodes+=1
        if visited_nodes == k:
            return node
        return dfs_helper(node.right)
        
    return dfs_helper(root)

def length_of_longest_substr(s: str) -> int:
    if len(s) < 2:
        return len(s)
    max_length = 0
    s_set = set()
    for s_char in s:
        s_set.add(s_char)
    i: int = 0
    for j in range(len(s)):
        if s[j] in s_set:
            s_set.remove(s[j])
            if j - i + 1 > max_length:
                max_length = j - i + 1
        else: 
            while(s[i] != s[j]):
                s_set.add(s[i])
                i+=1
            i += 1

    return max_length

assert length_of_longest_substr("abcabcbb") == 3
assert length_of_longest_substr("bbbbb") == 1
assert length_of_longest_substr("pwwkew") == 3
assert length_of_longest_substr("") == 0
assert length_of_longest_substr("au") == 2
assert length_of_longest_substr("dvdf") == 3

def subarray_sum(nums: list[int], k: int) -> int:
    if len(nums) == 0:
        return 0
    res: int = 0
    prefix_sum: int = 0
    prev_sums: dict[int, int] = {}

    for num in nums:
        prefix_sum += num
        if prefix_sum == k:
            res += 1
        if (prefix_sum - k) in prev_sums:
            res += prev_sums[prefix_sum - k]
        prev_sums[prefix_sum] = prev_sums.get(prefix_sum,0) + 1
    return res

assert subarray_sum([1,1,1], 2) == 2
assert subarray_sum([1,2,3], 3) == 2
assert subarray_sum([1], 0) == 0
assert subarray_sum([1,-1,0], 0) == 3
assert subarray_sum([1,2,1,2,1], 3) == 4