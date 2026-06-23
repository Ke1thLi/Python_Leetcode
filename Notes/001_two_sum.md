```markdown
# 1. 两数之和 (Two Sum)

> **难度**：简单 | **标签**：#哈希表 #数组 #经典必做

## 🎯 题目理解

在无序数组 `nums` 中找两个数，使其和等于 `target`，返回下标。  
**关键限制**：同一个元素不能用两次，且必有唯一解。

---

## 🧠 解题思路（由差到优的演进）

### 1. 暴力法（直觉）
- **想法**：固定一个数，遍历后面所有数看是否配对。
- **痛点**：每次找搭档都要重新遍历数组，做了大量重复工作。

### 2. 两遍哈希表（空间换时间）
- **想法**：先用字典存下所有数字的索引，再遍历数组查补数。
- **痛点**：需要额外判断 `hash_map[ant] != i`，防止查到自己是自己（如 `[3,3]` 场景）。

### 3. 一遍哈希表（最终最优解 ✅）
- **想法**：**边查边存**。遍历时，先问哈希表“我的补数来过吗？”，如果来过直接返回；如果没来过，把自己存进去等后面的数来问。
- **精髓**：因为当前数还没存入表，所以**绝对不会匹配到自己**，省去了下标判断。

---

## 💻 三种解法代码

```python
from typing import List

class Solution1:
    # 解法一：暴力破解
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_i in enumerate(nums):
            for j in range(i + 1, len(nums)):
                num_j = nums[j]
                if num_i + num_j == target:
                    return [i, j]
        return []


class Solution2:
    # 解法二：两遍哈希表（先存再查）
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        # 第一遍：把所有数字存入哈希表
        for i, num in enumerate(nums):
            num_to_index[num] = i
        # 第二遍：遍历查找补数
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index and num_to_index[complement] != i:
                return [i, num_to_index[complement]]
        return []


class Solution3:
    # 解法三：一遍哈希表（边查边存，最优）
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]  # 先返回之前的，再返回当前的
            num_to_index[num] = i
        return []
```

---

## 📁 源码文件

实际提交 LeetCode 的最终代码见：[源码](../Code/001_two_sum.py)

---

## 🔗 关联题目

- [167. 两数之和 II](./167_two_sum_ii.md)（**有序数组** → 双指针）

---

## 📝 个人总结（一句话唤醒记忆）

**无序数组找两数和 → 条件反射：一遍哈希表（边查边存）。**
```