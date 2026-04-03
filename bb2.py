from queue import Queue

def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    if len(nums) == 0:
        return 0
    
    helper_dict: dict[int, int] = {0: 1}
    prefix_sum: int = 0
    total_count: int = 0

    for num in nums:
        prefix_sum += num
        if helper_dict.get(prefix_sum - k) is not None:
            total_count += helper_dict[prefix_sum - k]
        helper_dict[prefix_sum] = helper_dict.get(prefix_sum, 0) + 1
    return total_count

class TreeNode:
    def __init__(self, val:int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    
    bfs_queue: Queue = Queue()
    bfs_queue.put(root)
    res: list[list[int]] = []

    while bfs_queue.qsize() > 0:
        q_size = bfs_queue.qsize()
        level: list[int] = []

        for _ in range(q_size):
            curr = bfs_queue.get()
            level.append(curr.val)
            if curr.left is not None:
                bfs_queue.put(curr.left)
            if curr.right is not None:
                bfs_queue.put(curr.right)
        res.append(level)

    return res

class ListNode:
    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    if l1 is None and l2 is None:
        return None
    
    l1_stack: list[int] = []
    l2_stack: list[int] = []

    curr: ListNode | None = l1
    while curr is not None:
        l1_stack.append(curr.val)
        curr = curr.next
    
    curr = l2
    while curr is not None:
        l2_stack.append(curr.val)
        curr = curr.next
    
    num_to_add = 0
    res: ListNode = ListNode(0)
    curr = res
    while len(l1_stack) > 0 or len(l2_stack) > 0 or num_to_add > 0:
        l1_val: int = 0
        if len(l1_stack) > 0:
            l1_val = l1_stack.pop()
        l2_val: int = 0
        if len(l2_stack) > 0:
            l2_val = l2_stack.pop()
        val_to_create = num_to_add + l1_val + l2_val
        curr.next = ListNode(val_to_create % 10)
        num_to_add = val_to_create // 10
        curr = curr.next

    return res.next

def max_area(height: list[int]) -> int:
    if len(height) < 2:
        return 0
    max_val: int = 0
    start:int = 0
    end:int = len(height)-1

    while end > start:
        curr_val = min(height[start], height[end]) * (end - start)
        if curr_val > max_val:
            max_val = curr_val
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1

    return max_val

def search(nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    
    def get_invalid_index(start: int, end: int, min_val: int, max_val: int) -> int:
        if start > end:
            return -1
        if start == end:
            if nums[start] < min_val or nums[start] > max_val:
                return start
            return -1
        mid = (end + start) // 2
        if nums[mid] < min_val or nums[mid] > max_val:
            return mid
        left_part = get_invalid_index(start, mid-1, min_val, nums[mid])
        if left_part > -1:
            return left_part
        return get_invalid_index(mid+1, end, nums[mid], max_val)
    
    def binary_search(start: int, end: int) -> int:
        if start > end:
            return -1
        mid = (end + start) // 2
        if(nums[mid] == target):
            return mid
        if(nums[mid] > target):
            return binary_search(start, mid-1)
        return binary_search(mid+1, end)
    
    invalid_index = get_invalid_index(0, len(nums)-1, nums[0], nums[len(nums)-1])
    if invalid_index == -1:
        return binary_search(0, len(nums)-1)

    part1_res = binary_search(0, invalid_index)
    if part1_res > -1:
        return part1_res
    return binary_search(invalid_index+1, len(nums)-1)

def num_islands(grid: list[list[str]]) -> int:
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    visited_grid: list[list[bool]] = []
    for row in range(len(grid)):
        visited_grid.append([False] * len(grid[row]))
    total_islands: int = 0

    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column == "1" and visited_grid[i][j] == False:
                bfs_queue: list[tuple[int, int]] = [(i,j)]
                total_islands += 1
                while len(bfs_queue) > 0:
                    curr = bfs_queue.pop(0)
                    if(visited_grid[curr[0]][curr[1]] == True): 
                        continue
                    visited_grid[curr[0]][curr[1]] = True
                    if curr[0]-1 >= 0 and visited_grid[curr[0]-1][curr[1]] == False and grid[curr[0]-1][curr[1]] == "1":
                        bfs_queue.append((curr[0]-1, curr[1]))
                    if curr[0]+1 < len(grid) and visited_grid[curr[0]+1][curr[1]] == False and grid[curr[0]+1][curr[1]] == "1":
                        bfs_queue.append((curr[0]+1, curr[1]))
                    if curr[1]-1 >= 0 and visited_grid[curr[0]][curr[1]-1] == False and grid[curr[0]][curr[1]-1] == "1":
                        bfs_queue.append((curr[0], curr[1]-1))
                    if curr[1]+1 < len(row) and visited_grid[curr[0]][curr[1]+1] == False and grid[curr[0]][curr[1]+1] == "1":
                        bfs_queue.append((curr[0], curr[1]+1))
    return total_islands

def daily_temperatures(t: list[int]) -> list[int]:
    if len(t) == 0:
        return []
    if len(t) == 1:
        return [0]
    
    helper_stack: list[tuple[int, int]] = []
    res: list[int] = [0] * len(t)
    for i in range(len(t)-1,-1,-1):
        found_larger: bool = False
        while not found_larger and len(helper_stack) > 0:
            if helper_stack[-1][0] > t[i]:
                found_larger = True
                res[i] = helper_stack[-1][1] - i
            else:
                helper_stack.pop()
        helper_stack.append((t[i], i))
    return res

def merge(intervals: list[tuple[int,int]]) -> list[tuple[int, int]]:
    if len(intervals) < 2:
        return intervals
    intervals.sort(key = lambda x: x[0])
    res: list[tuple[int, int]] = []
    i: int = 0
    while i < len(intervals):
        if i == len(intervals)-1:
            res.append(intervals[i])
            break
        j=i+1
        while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
            j += 1
        res.append([intervals[i][0], max(intervals[i][1], intervals[j-1][1])])
        i = j
    return res

def check_subarray_sum(nums: list[int], k: int) -> bool:
    if len(nums) == 0:
        return False
    helper_dict: dict[int, int] = {0: -1}
    sum_prefix = 0
    for i, num in enumerate(nums):
        sum_prefix += num
        if helper_dict.get(sum_prefix % k) is not None and i - helper_dict[sum_prefix % k] > 1:
            return True
        if helper_dict.get(sum_prefix % k) is None:
            helper_dict[sum_prefix % k] = i
    return False

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    if len(preorder) == 0: 
        return None
    inorder_dict: dict[int, int] = {}
    for i, num in enumerate(inorder):
        inorder_dict[num] = i
    def build_tree_helper(pre_start: int, pre_end: int, in_start:int, in_end: int) -> TreeNode | None:
        if pre_start > pre_end:
            return None
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])
        res = TreeNode(preorder[pre_start])
        head_subtree_index = inorder_dict[res.val]
        left_subtree_size = head_subtree_index - in_start
        if left_subtree_size > 0:
            res.left = build_tree_helper(pre_start + 1, pre_start + left_subtree_size,head_subtree_index-left_subtree_size,head_subtree_index-1)
        right_subtree_size = in_end - head_subtree_index
        if right_subtree_size > 0:
            res.right = build_tree_helper(pre_end - right_subtree_size + 1, pre_end, head_subtree_index+1,head_subtree_index+right_subtree_size)
        return res

    return build_tree_helper(0, len(preorder)-1, 0, len(inorder)-1)

def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    if head is None:
        return head
    before_left = None
    curr = head
    while curr is not None and curr.val != left:
        before_left = curr
        curr = curr.next
    if curr is None:
        return head

    start_node = curr
    prev = before_left

    while curr and curr.val != right:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    start_node.next = curr.next
    curr.next = prev

    if before_left:
        before_left.next = curr
        return head
    return curr

def reverse(head: ListNode | None):
    if head is None:
        return None

    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = reverse_between(l1, 2, 4)
vals = []
curr = result
while curr:
    vals.append(curr.val)
    curr = curr.next
assert vals == [1, 4, 3, 2, 5]

l2 = ListNode(5)
result2 = reverse_between(l2, 5, 5)
assert result2.val == 5

l3 = ListNode(1, ListNode(2))
result3 = reverse_between(l3, 1, 2)
vals3 = []
curr = result3
while curr:
    vals3.append(curr.val)
    curr = curr.next
assert vals3 == [2, 1]

def longest_con_seq(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    
    helper_set = set(nums)
    
    max_length = 0

    for num in nums:
        if num-1 not in helper_set:
            current_len = 1
            val = num+1
            while val in helper_set:
                current_len +=1
                val +=1
            if current_len > max_length:
                max_length = current_len

    return max_length
