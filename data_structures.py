def func(nums: list[int]) -> int:
    if len(nums) == 0:
        return -1
    max_val: int = nums[0]
    def helper_func():
        nonlocal max_val # this is how to update original value (by ref)
        for num in nums:
            if num > max_val:
                max_val = num
    helper_func()
    return max_val


class TreeNode:
    def __init__(self, val: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

# array
arr: list[int] = [2, 3, 3]
arr.append(5)
print(arr) # 2, 3, 3, 5
arr.pop()
print(arr) # 2, 3, 3
print(arr[::-1]) # 3, 3, 2

# hash/dict
person: dict[str,str] = {'name':'John', 'color':'blue'}
print(person['color'])
person['food'] = '🍓'
print(person.get('food')) # safer, return None is not exists
if 'name' in person:
    print(person['name'])

# set
fruits: set[str] = set()
fruits.add('🍏')
fruits.add('🍓')
fruits.add('🍏')
if '🍌' not in fruits:
    print(fruits)

seen: set[int] = set(arr)
print(seen) # 2, 3

# stack
stack: list[int] = []
stack.append(1)
stack.append(3)
stack.append(5)
top:int = stack.pop()
print(top)
print(stack)
print(f'peek {stack[-1]}')

# queue
from collections import deque
q = deque()
q.append(1)
q.append(3)
q.append(5)
print(q[0]) # peek without remove
print(q.popleft())
print(q)

# nonlocal, append