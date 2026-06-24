"""
LeetCode 1: 两数之和
核心：一遍哈希表（边查边存，空间换时间）
复杂度：O(n) 时间 | O(n) 空间
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []