# 26. 删除有序数组中的重复项

> **难度**：简单 | **标签**：#数组 #双指针

## 题目理解

给定一个升序排列的数组 nums，要求原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。不能使用额外数组空间，必须原地修改输入数组。

关键限制：O(1) 额外空间。

---

## 我的解法

### 解法一：嵌套循环移位法（首次提交，超时）

- **思路**：用 i 遍历数组，当 nums[i] 与 nums[i-1] 重复时，将 i 之后的元素全部前移一位覆盖重复项，同时缩减数组长度 size。
- **关键变量**：`i` 为当前检查位置，`size` 为当前有效数组长度，内层循环负责搬运元素。
- **复杂度**：O(n^2) 时间 | O(1) 空间

**问题**：每次遇到重复元素都要执行 O(n) 的移位操作，最坏情况下（如全部元素相同）复杂度退化为 O(n^2)，大规模输入下超时。

### 解法二：快慢指针（最终提交，AC）

- **思路**：用 slow 指针维护「不重复区间」的右边界，fast 指针扫描整个数组。当 fast 遇到新元素时，slow 前移并复制该元素。
- **关键变量**：`slow` 指向当前不重复区间的最后一个位置，`fast` 遍历数组寻找新元素。
- **复杂度**：O(n) 时间 | O(1) 空间

**优化点**：将 O(n) 的移位操作降为 O(1) 的覆盖赋值，整体从 O(n^2) 降到 O(n)。

## 代码

### 解法一代码（超时）

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        i = 1
        while i < size:
            if nums[i]  == nums[i-1]:
                for j in range(i+1, size):
                    nums[j-1] = nums[j]
                size -= 1
            else:
                i += 1
        return size
```

### 解法二代码（AC）

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
```

---

## 易错点 / 边界细节

- 解法一：移位后 `i` 不能前进，因为新移来的元素还需比较。
- 解法二：`slow` 指向的是不重复区间的**最后一个位置**，所以返回长度是 `slow + 1`。
- 解法二利用了**有序数组**的前提 —— 重复元素必定相邻，不需要哈希表。

---

## 关联题目

- [源码](../Code/26.删除有序数组中的重复项.py)

---

## 一句话总结

快慢指针，慢针守住不重复区，快针探路，遇新就收。