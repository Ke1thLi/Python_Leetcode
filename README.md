# Python_Leetcode

> Python 算法刷题笔记，一题多解 + 深度复盘。

---

## 当前进度（Python）

| 编号 | 题目名称 | 难度 | 最优解法 | 笔记 | 源码 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 两数之和 | 简单 | 一遍哈希表 | [笔记](./Notes/001_two_sum.md) | [源码](./Code/001_two_sum.py) |
| 167 | 两数之和 II | 中等 | 双指针（对撞） | [笔记](./Notes/167_two_sum_ii.md) | [源码](./Code/167_two_sum_ii.py) |
| 209 | 长度最小的子数组 | 中等 | 滑动窗口 | [笔记](./Notes/209_min_size_subarray_sum.md) | [源码](./Code/209.长度最小的子数组.py) |
| 3 | 无重复字符的最长子串 | 中等 | 滑动窗口 | [笔记](./Notes/3_longest_substring_without_repeating_characters.md) | [源码](./Code/3.无重复字符的最长子串.py) |
| 26 | 删除有序数组中的重复项 | 简单 | 快慢指针 | [笔记](./Notes/26_remove_duplicates_from_sorted_array.md) | [源码](./Code/26.删除有序数组中的重复项.py) |
| 704 | 二分查找 | 简单 | 二分查找 | [笔记](./Notes/704_binary_search.md) | [源码](./Code/704.二分查找.py) |

---

## 核心口诀

- 无序数组找两数 → 哈希表
- 有序数组找两数 → 双指针（对撞）
- 最短连续子数组 → 滑动窗口（同向双指针）
- 无重复子串最长长度 → 滑动窗口 + 哈希表记录字符位置
- 有序数组去重 → 快慢指针，慢指针维护不重复区边界
- 有序数组查找目标 → 二分查找（暴力遍历可做，但升序数组天生适合二分）

---

## 专题地图

- 哈希表：[001. 两数之和](./Notes/001_two_sum.md)
- 双指针：[167. 两数之和 II](./Notes/167_two_sum_ii.md)
- 滑动窗口：[209. 长度最小的子数组](./Notes/209_min_size_subarray_sum.md)
- 滑动窗口（字符串）：[3. 无重复字符的最长子串](./Notes/3_longest_substring_without_repeating_characters.md)
- 快慢指针：[26. 删除有序数组中的重复项](./Notes/26_remove_duplicates_from_sorted_array.md)
- 二分查找：[704. 二分查找](./Notes/704_binary_search.md)

---

## 下一题推荐

> [59. 螺旋矩阵 II](./Notes/59_spiral_matrix_ii.md)
> 理由：你主动选的，模拟数组遍历，练习对循环不变量的控制。