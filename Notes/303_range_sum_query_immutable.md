# 303. 区域和检索 - 数组不可变

> **难度**：简单 | **标签**：#数组 #设计 #前缀和

## 题目理解

设计一个 `NumArray` 类，支持初始化一个整数数组和查询任意区间 `[left, right]` 的元素和。数组不可变（没有更新操作），但查询次数可能很多。

---

## 我的解法

### 解法一：暴力遍历（每次查询 O(n)）

- **思路**：`sumRange` 方法中根据传入的 `left` 和 `right`，每次通过 for 循环遍历区间累加求和。
- **关键变量**：`tot` 为累加器，用于统计区间内元素之和。
- **复杂度**：O(n) 时间（每次 `sumRange` 调用） | O(1) 空间（不含存放原始数组的空间）

注：后续优化版本依次记为解法二、解法三……保留所有已提交的版本。

### 解法二：前缀和预处理（每次查询 O(1)）

- **思路**：在构造函数中预先计算前缀和数组 `prefix`，其中 `prefix[i]` 表示 `nums[0..i-1]` 的前缀和（即前 i 个元素之和）。这样区间 `[left, right]` 的和就等于 `prefix[right+1] - prefix[left]`，每次查询只需 O(1) 时间。
- **关键变量**：`prefix` 数组，长度比原数组多 1，`prefix[i]` 存储前 i 个元素的和。
- **复杂度**：O(n) 预处理时间 | O(n) 空间（前缀和数组），每次 `sumRange` 查询 O(1) 时间

## 代码

### 解法一：暴力遍历

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        tot = 0
        for k in range(left, right + 1):
            tot += self.nums[k]
        return tot
```

### 解法二：前缀和优化

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
```

---

## 易错点 / 边界细节

- 区间 `[left, right]` 是闭区间，前缀和公式为 `prefix[right+1] - prefix[left]`，注意索引偏移。
- `prefix` 数组长度为 `len(nums) + 1`，`prefix[0] = 0` 作为哨兵，避免对 left=0 时单独处理。
- 暴力解法在查询次数少时够用，但 m 次查询总复杂度 O(m * n)；前缀和预处理后每次查询 O(1)，适合查询频繁的场景。
- `NumArray` 构造时直接保存引用即可，数组不可变保证了前缀和的有效性。

---

## 关联题目

- [209. 长度最小的子数组](./209_min_size_subarray_sum.md) — 滑动窗口，涉及连续子数组和
- [560. 和为 K 的子数组] — 前缀和 + 哈希表进阶
- [1109. 航班预订统计] — 差分数组（前缀和的变体应用）

---

## 源码文件

[源码](../Code/303.区域和检索-数组不可变.py)

---

## 一句话总结

暴力遍历 O(n) 查询 → 前缀和预处理 O(1) 查询，用空间换时间是区间求和问题的标准优化路径。
