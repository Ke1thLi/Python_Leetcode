# 3. 无重复字符的最长子串

> **难度**：中等 | **标签**：#字符串 #滑动窗口 #哈希表

## 题目理解

给定一个字符串 `s`，找出其中**不含有重复字符**的**最长子串**的长度。

关键限制：子串要求连续，且字符不能重复。字符串只包含 ASCII 字符（或 Unicode，但通常用 ASCII 范围测试）。

---

## 我的解法

### 解法一：暴力枚举

- **思路**：固定起点 i，从 i 开始向右遍历 j，用 Set 记录已出现的字符。如果 s[j] 已经在 Set 中，则当前 i 的枚举结束。每轮更新最长长度。
- **关键变量**：`i` 子串起点，`j` 子串终点，`seen` 当前窗口内的字符集合，`max_len` 最长长度。
- **复杂度**：O(n^2) 时间 | O(min(n, |Σ|)) 空间（|Σ| 为字符集大小）

### 解法二：滑动窗口（Set + 同向双指针，外层 while + if/else）

- **思路**：用 left/right 两个指针维护一个无重复字符的窗口，外层 while 循环驱动。right 尝试前进，如果 s[right] 已在窗口内，则 left 右移缩小窗口（从 seen 中移除 s[left]），直到右指针处字符不再重复；否则将 s[right] 加入 seen，更新最大长度，right 右移。
- **关键变量**：`left/right` 窗口左右边界，`seen` 当前窗口内字符的集合，`max_len` 最长长度。
- **复杂度**：O(n) 时间（每个字符最多被 left 和 right 各访问一次）| O(min(n, |Σ|)) 空间

### 解法三：滑动窗口（Set + 同向双指针，for + 内层 while）

- **思路**：用 for 循环驱动 right 自动前进（无需手动维护 right 右移），right 每次进入后先用内层 while 把窗口中的冲突字符清空（循环移除 s[left] 并 left++），然后将当前字符加入 seen。
- **与解法二的区别**：解法二用 `while + if/else`，right 发现冲突只移一个 left 就回到循环条件判断，相当于逐次试探；解法三用 `for + 内层 while`，right 永远自动前进，冲突时一口气清空，控制流更简洁。
- **复杂度**：O(n) 时间 | O(min(n, |Σ|)) 空间

---

## 代码

```python
# 解法一：暴力枚举
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)
        return max_len


# 解法二：滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
        return max_len


# 解法三：滑动窗口（for + 内层 while）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
```

---

## 易错点 / 边界细节

1. **空字符串**：s = "" 时三种解法都返回 0。
2. **全相同字符**：如 "aaaaa"，暴力解每轮 break；解法二 right 不动 left 一直右移；解法三 for 循环每次 right 自动 +1，内层 while 连续移除。
3. **暴力解性能**：O(n^2) 在大输入时可能超时。
4. **滑动窗口 left 移动**：都是逐次右移 left 并 remove，不是跳跃式。
5. **解法二 vs 解法三的控制流差异**：解法二的 right 在冲突时不前进（停在原地等 left 腾位置）；解法三的 right 永远前进（靠 for 自动 +1），冲突由内层 while 处理。两种写法等价，但解法三更简洁，且不会有忘记 right++ 的风险。

---

## 关联题目

- [已刷的关联题](./001_two_sum.md)
- [已刷的关联题](./167_two_sum_ii.md)
- [已刷的关联题](./209_min_size_subarray_sum.md)

---

## 源码文件

[源码](../Code/3.无重复字符的最长子串.py)

---

## 一句话总结

暴力枚举 O(n^2)；滑动窗口两种写法（while+if 与 for+内层 while）等价，后者更简洁。
