"""
LeetCode 167: 两数之和 II - 输入有序数组
核心：有序数组 -> 双指针（对撞指针，空间换时间的最优解）
复杂度：O(n) 时间 | O(1) 空间
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:  # ✅ 标准写法，指针永远不会交叉
            the_sum = numbers[left] + numbers[right]
            if the_sum == target:
                return [left + 1, right + 1]
            elif the_sum > target:
                right -= 1
            else:  # the_sum < target
                left += 1
        return []