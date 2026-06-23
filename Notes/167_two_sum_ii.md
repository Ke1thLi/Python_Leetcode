```markdown
# 167. 两数之和 II - 输入有序数组 (Two Sum II - Input Array Is Sorted)

> **难度**：中等 | **标签**：#双指针 #数组 #有序数组

---

## 🎯 题目理解

给定一个**已按非递减顺序排列**的整数数组 `numbers`，找出两个数使它们的和等于目标数 `target`。

**关键区别**（与第 1 题对比）：
- 数组是**有序**的（升序/非递减）
- 下标**从 1 开始计数**，返回 `[index1, index2]` 且 `index1 < index2`
- 要求**只使用常量级的额外空间**（O(1)）

---

## 🧠 解法一：双指针（对撞指针）✅ 最优解

### 核心思想
利用数组**有序**的特性，用两个指针分别指向数组的**最左端（最小值）** 和最右端（最大值），然后向中间移动。

### 移动规则
1. 计算 `sum = numbers[left] + numbers[right]`
2. 如果 `sum == target` → 找到答案，返回 `[left+1, right+1]`
3. 如果 `sum < target` → 和太小，`left` 右移（让和变大）
4. 如果 `sum > target` → 和太大，`right` 左移（让和变小）

### 为什么双指针不会漏掉解？
因为数组有序，每次移动指针相当于**消去了一整行或一整列不可能的解**，保证了算法的正确性。

---

## 💻 代码（解法一：双指针）

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:          # 对撞指针，直到相遇
            the_sum = numbers[left] + numbers[right]
            
            if the_sum == target:
                return [left + 1, right + 1]  # 下标从 1 开始
            elif the_sum > target:
                right -= 1           # 和太大，右指针左移
            else:                    # the_sum < target
                left += 1            # 和太小，左指针右移
        
        return []
```

---

## 💻 解法二：哈希表（备胎思路）

> **适用场景**：如果题目没有"常数空间"的限制，或者数组不是有序的（回到第 1 题），这套哈希表逻辑依然能打。

- **想法**：沿用第 1 题的"边查边存"思路，用字典存储数字到下标的映射。
- **关键改动**：因为本题要求返回下标从 **1** 开始，所以**存的时候直接存 `i + 1`**，取出来直接就是 1 基下标，再也不用手动加 1。
- **复杂度**：O(n) 时间 | O(n) 空间（**不满足**本题 O(1) 的进阶要求，因此仅作对比学习）。

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_to_index:
                # 因为存的时候就是 1 基，所以这里直接取，当前 i 转成 1 基
                return [num_to_index[complement], i + 1]
            # 存的时候直接转成 1 基，一劳永逸
            num_to_index[num] = i + 1
        return []
```

---

## 📊 复杂度对比

| 解法 | 时间复杂度 | 空间复杂度 | 是否满足进阶要求 |
| :--- | :--- | :--- | :--- |
| **双指针（解法一）** | **O(n)** | **O(1)** | ✅ **满足（最优解）** |
| 哈希表（解法二） | O(n) | O(n) | ❌ 不满足（仅作思路拓展） |

---

## ⚠️ 易错点 / 关键细节

1. **下标从 1 开始**：双指针返回时一定要 `+1`；哈希表解法存的时候直接存 `i+1`，避免混淆。
2. **while 条件**：必须用 `left < right`，不能用 `<=`，否则两个指针指向同一个元素（重复使用），破坏对撞语义。
3. **指针移动方向**：
   - 和太小 → 左指针右移（`left += 1`）
   - 和太大 → 右指针左移（`right -= 1`）
4. **题目保证有唯一解**，所以不需要担心找不到答案的边界情况，`return []` 只是兜底。

---

## 🔗 关联题目（知识串联）

- [001. 两数之和](./001_two_sum.md)（**无序数组** → 哈希表）
- 当前题目（**有序数组** → 双指针）

---

## 📝 个人总结（一句话唤醒记忆）

**有序数组找两数和 → 条件反射：双指针（对撞指针，O(1) 空间）。**
```