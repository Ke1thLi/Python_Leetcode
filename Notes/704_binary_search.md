# 704. 二分查找

> **难度**：简单 | **标签**：#数组 #二分查找

## 题目理解

给定一个升序整数数组 `nums` 和一个目标值 `target`，返回 `target` 在数组中的索引，不存在则返回 -1。要求实现 O(log n) 时间复杂度的算法。

关键限制：数组已升序排列。

---

## 我的解法

### 解法一：暴力遍历（线性查找）

- **思路**：直接遍历整个数组，逐个比较每个元素与目标值，找到则返回当前索引，遍历结束未找到返回 -1。
- **关键变量**：`i` 为当前遍历到的索引，`num` 为当前元素值。
- **复杂度**：O(n) 时间 | O(1) 空间

注：后续优化版本依次记为解法二、解法三……保留所有已提交的版本。

### 解法二：二分查找（左闭右开区间）

- **思路**：利用数组升序性质，每次取中间值与 target 比较，将搜索范围缩小一半。使用 `[left, right)` 左闭右开区间模板，`right` 初始为 `len(nums)`，循环条件为 `left < right`。
- **关键变量**：`left` 指向当前搜索区间的左边界（包含），`right` 指向右边界（不包含），`mid` 为中间索引。
- **复杂度**：O(log n) 时间 | O(1) 空间

### 解法三：二分查找（左闭右闭区间）

- **思路**：同样基于二分思想，使用 `[left, right]` 左闭右闭区间模板，`right` 初始为 `len(nums) - 1`，循环条件为 `left <= right`，收缩时右边界为 `mid - 1`。
- **关键变量**：`left` 为左边界（包含），`right` 为右边界（包含），`mid` 为中间索引。
- **复杂度**：O(log n) 时间 | O(1) 空间

## 代码

### 暴力遍历

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
```

### 二分查找（左闭右开）

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = (left + right) // 2
        while left < right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            mid = (left + right) // 2

        return -1
```

### 二分查找（左闭右闭）

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1
```

---

## 易错点 / 边界细节

- 遍历完后一定要返回 -1，表示未找到，不能遗漏这个 return
- 左闭右开模板（解法二）：`right = len(nums)`，循环 `while left < right`，收缩 `right = mid`（不包含 mid 本身）
- 左闭右闭模板（解法三）：`right = len(nums) - 1`，循环 `while left <= right`，收缩 `right = mid - 1`
- 两个模板的核心区别在于右边界是否包含，决定了初始值、循环条件、收缩方式的差异

---

## 关联题目

- [已刷的关联题](./001_two_sum.md)（两数之和也用到了数组遍历）
- [下一题推荐](./59_spiral_matrix_ii.md)
- [35. 搜索插入位置](./35_search_insert_position.md)（二分查找的变体，练习二分模板的进阶题）

---

## 源码文件

[源码](../Code/704.二分查找.py)

---

## 一句话总结

暴力遍历 → 二分查找，掌握左闭右开和左闭右闭两种模板，核心是区间定义决定了边界处理。
