# Python_Leetcode

> Python 算法刷题笔记，一题多解 + 深度复盘。

---

## 当前进度（Python）

| 编号 | 题目名称 | 难度 | 最优解法 | 笔记 | 源码 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 两数之和 | 简单 | 一遍哈希表 | [笔记](./Notes/001_two_sum.md) | [源码](./Code/001_two_sum.py) |
| 167 | 两数之和 II | 中等 | 双指针（对撞） | [笔记](./Notes/167_two_sum_ii.md) | [源码](./Code/167_two_sum_ii.py) |
| 209 | 长度最小的子数组 | 中等 | 滑动窗口 | [笔记](./Notes/209_min_size_subarray_sum.md) | [源码](./Code/209.长度最小的子数组.py) |

---

## 核心口诀

- 无序数组找两数 → 哈希表
- 有序数组找两数 → 双指针（对撞）
- 最短连续子数组 → 滑动窗口（同向双指针）

---

## 专题地图

- 哈希表：[001. 两数之和](./Notes/001_two_sum.md)
- 双指针：[167. 两数之和 II](./Notes/167_two_sum_ii.md)
- 滑动窗口：[209. 长度最小的子数组](./Notes/209_min_size_subarray_sum.md)

---

## 下一题推荐

> [3. 无重复字符的最长子串](./Notes/3_longest_substring_without_repeating_characters.md)  
> 理由：滑动窗口换场景，从「数值累加和 >= target」变成「窗口内字符不重复」。