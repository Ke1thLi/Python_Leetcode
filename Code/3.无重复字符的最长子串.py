'''
LeetCode 3: 无重复字符的最长子串
核心： 子串查重 -> 双指针（滑动窗口，用哈希集合辅助实现 O(1) 查重，空间换时间的最优解）
复杂度： O(n) 时间 | O(1) 空间（字符集固定，如 ASCII 为 128 或 256）
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):  # right 用 for 循环自动前进
            # 只要重复，就一直移动 left 并删除，直到没有重复
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

# @lc code=end

