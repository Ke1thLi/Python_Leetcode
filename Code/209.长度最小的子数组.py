"""
LeetCode 209: 长度最小的子数组
核心：滑动窗口<同向双指针),O(n) 时间 | O(1) 空间
"""
#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        min_len = float('inf')
        while right < len(nums):
            total += nums[right]
            while total >= target:
                min_len = min(min_len,right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return 0 if min_len == float('inf') else min_len

        
# @lc code=end

