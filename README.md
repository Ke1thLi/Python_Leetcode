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
| 59 | 螺旋矩阵 II | 中等 | 方向向量模拟 | [笔记](./Notes/59_spiral_matrix_ii.md) | [源码](./Code/59.螺旋矩阵-ii.py) |
| 303 | 区域和检索 - 数组不可变 | 简单 | 前缀和 | [笔记](./Notes/303_range_sum_query_immutable.md) | [源码](./Code/303.区域和检索-数组不可变.py) |

---

## 核心口诀

- 无序数组找两数 → 哈希表
- 有序数组找两数 → 双指针（对撞）
- 最短连续子数组 → 滑动窗口（同向双指针）
- 无重复子串最长长度 → 滑动窗口 + 哈希表记录字符位置
- 有序数组去重 → 快慢指针，慢指针维护不重复区边界
- 有序数组查找目标 → 二分查找（暴力遍历可做，但升序数组天生适合二分）
- 矩阵螺旋填充 → 方向向量带路走，撞墙右转不停步
- 区间求和多次查 → 前缀和数组 O(1) 拿下

---

## 专题地图

- 哈希表：[001. 两数之和](./Notes/001_two_sum.md)
- 双指针：[167. 两数之和 II](./Notes/167_two_sum_ii.md)
- 滑动窗口：[209. 长度最小的子数组](./Notes/209_min_size_subarray_sum.md)
- 滑动窗口（字符串）：[3. 无重复字符的最长子串](./Notes/3_longest_substring_without_repeating_characters.md)
- 快慢指针：[26. 删除有序数组中的重复项](./Notes/26_remove_duplicates_from_sorted_array.md)
- 二分查找：[704. 二分查找](./Notes/704_binary_search.md)
- 前缀和：[303. 区域和检索 - 数组不可变](./Notes/303_range_sum_query_immutable.md)

---

## 下一题推荐

> [1109. 航班预订统计](./Notes/1109_corporate_flight_bookings.md)
> 理由：差分数组是前缀和的逆向思维——前缀和用于多次区间查询，差分数组用于多次区间修改后的一次性查询。做完 303 的前缀和，接着学差分数组正好衔接。