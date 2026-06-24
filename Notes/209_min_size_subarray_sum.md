# 209. 长度最小的子数组

> **难度**：中等 | **标签**：#数组 #滑动窗口 #双指针

## 题目理解

给定一个正整数数组 `nums` 和一个正整数 `target`，找出数组中满足其和 >= target 的**长度最小**的连续子数组，返回其长度。如果不存在则返回 0。

关键限制：全是正整数，窗口扩大时和单调递增，缩小时和单调递减——这是滑动窗口能用的前提。

---

## 我的解法

### 解法一：暴力枚举（首次提交，超时）

- **思路**：固定起点 i，从 i 开始向右累加，一旦和 >= target 就更新最小长度并 break。
- **复杂度**：O(n^2) 时间 | O(1) 空间
- **结果**：大数组超时。

### 解法二：滑动窗口（AC）

- **思路**：用两个指针维护一个窗口，right 不断右移扩大窗口累加和。当窗口内和 >= target 时，记录当前长度，然后左移 left 缩小窗口（减去 nums[left]），直到和 < target。
- **关键变量**：`left/right` 窗口左右边界，`total` 窗口内元素和，`min_len` 最短长度。
- **复杂度**：O(n) 时间（每个元素最多被 left 和 right 各访问一次）| O(1) 空间

## 代码

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        min_len = float('inf')
        while right < len(nums):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return 0 if min_len == float('inf') else min_len
```

> 注意：两重循环不一定是 O(n^2)，这里每个元素最多被 left 和 right 各访问一次，所以是 O(n)。

---

## 易错点 / 边界细节

1. **全是正整数** 是滑动窗口成立的前提（和单调递增/递减）。
2. while 收缩条件用 `>=` 而不是 `>`，等于 target 时也要收缩记录。
3. right 指针在每次循环末尾固定 +1，确保每个元素恰好被 right 经过一次。
4. 最后返回时判断 `min_len` 是否为 `inf`，是则返回 0。

---

## 关联题目

- [已刷的关联题](./001_two_sum.md)

---

## 源码文件

[源码](../Code/209.长度最小的子数组.py)

---

## 一句话总结

同向双指针滑动窗口，右扩左缩 O(n) 过。
