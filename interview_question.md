# Interview Question: Range Product

You are given four inputs:

* `n` – the length of the arrays
* `k` – a modulus
* `dir` – an array of length `n`, each element is `'L'` or `'R'`
* `nums` – an array of length `n` containing integers

You maintain two pointers:

```
left = 0
right = n - 1
```

These pointers define the active range `nums[left..right]`.

For each step `i` from `0` to `n - 1`:

* If `dir[i] == 'L'`, remove `nums[left]` and set `left += 1`.
* If `dir[i] == 'R'`, remove `nums[right]` and set `right -= 1`.

After the removal at step `i`:

* `res[i]` is the product of all active numbers `nums[left..right]` modulo `k`.
* If no numbers are active (`left > right`), the product is defined as `1`.

Return the array `res` of length `n`.

---

## Example

**Input**

```
n = 5
k = 7
nums = [3, 4, 2, 5, 6]
dir  = ['L', 'R', 'L', 'L', 'R']
```

**Step 0**
Remove from left (3).
Active: [4, 2, 5, 6]
Product = 4*2*5*6 = 240 → 240 % 7 = 2

**Step 1**
Remove from right (6).
Active: [4, 2, 5]
Product = 40 → 40 % 7 = 5

**Step 2**
Remove from left (4).
Active: [2, 5]
Product = 10 → 10 % 7 = 3

**Step 3**
Remove from left (2).
Active: [5]
Product = 5 → 5 % 7 = 5

**Step 4**
Remove from right (5).
Active: []
Product of empty = 1

**Output**

```
[2, 5, 3, 5, 1]
```
