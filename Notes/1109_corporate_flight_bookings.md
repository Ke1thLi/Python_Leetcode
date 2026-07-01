# 1109. 航班预订统计

> **难度**：中等 | **标签**：#数组 #差分数组 #前缀和

## 题目理解

给定 `n` 个航班（编号 1~n），和一个预订列表 `bookings`，每个预订 `[first, last, seats]` 表示从 `first` 到 `last`（含）的每个航班都预订了 `seats` 个座位。返回长度为 `n` 的数组 `answer`，其中 `answer[i]` 是航班 `i+1` 的预订座位总数。

关键限制：n 和 bookings 长度最多 2x10^4，每个 booking 区间跨度可能接近 n，暴力法会超时。

---

## 我的解法

### 解法一：暴力遍历（超时 TLE）

- **思路**：遍历每个 booking，在其覆盖的航班区间上逐个累加座位数。最坏情况下每个 booking 都跨越所有航班，复杂度 O(N*K)，N=2x10^4、K=2x10^4 时总操作约 4x10^8 次，Python 无法承受。
- **关键变量**：`ans` 数组维护每个航班的累计座位数。
- **复杂度**：O(N*K) 时间 | O(N) 空间（不含输入）

注：后续优化版本依次记为解法二、解法三……保留所有已提交的版本。

### 解法二：差分数组（AC）

- **思路**：差分数组专门处理「多次区间增减，一次查询结果」的问题。在 `diff` 数组上，区间 `[l, r]` 加 val 只需 `diff[l] += val`、`diff[r+1] -= val`，最后前缀和还原即得每个位置的最终值。
- **关键变量**：`diff` 长度为 n+1（多一位避免越界），`curr` 为累加器，一边遍历一边计算当前航班的总座位数。
- **复杂度**：O(N+K) 时间 | O(N) 空间（差分数组）

## 代码

### 解法一：暴力遍历（TLE）

```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for first, last, seats in bookings:
            for i in range(first - 1, last):
                ans[i] += seats
        return ans
```

### 解法二：差分数组（AC）

```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats
        ans = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            ans[i] = curr
        return ans
```

---

## 易错点 / 边界细节

- 航班编号从 1 开始，数组索引从 0 开始，注意 `first - 1` 到 `last - 1` 的偏移。
- 暴力法虽然逻辑直观，但 Python 双层循环在数据量达到 2x10^4 时会超时，需要差分数组优化到 O(N+K)。
- 差分数组 `diff` 长度设为 `n+1`，在 `diff[last] -= seats` 时利用了多出的一个位置，避免对 `last == n` 做特判。
- 还原时用 `curr` 累加 `diff[i]`，本质上就是前缀和还原。`diff[i]` 表示位置 `i` 相对于 `i-1` 的变化量。

---

## 关联题目

- [303. 区域和检索 - 数组不可变](./303_range_sum_query_immutable.md) — 前缀和（差分数组的逆向思维）
- [1094. 拼车] — 差分数组同场景练习

---

## 源码文件

[源码](../Code/1109.航班预订统计.py)

---

## 一句话总结

区间多次累加，暴力双循环超时 → 差分数组 O(1) 修改 O(N) 还原，前缀和的逆向思维。
