# 59. 螺旋矩阵 II

> **难度**：中等 | **标签**：#矩阵 #模拟

## 题目理解

给定正整数 `n`，生成一个包含 1 到 n^2 所有元素且按顺时针顺序螺旋排列的 n x n 正方形矩阵。

关键限制：必须原地构建矩阵，按层（圈）或方向模拟填充过程。

---

## 我的解法

### 解法一：按层模拟（四指针收缩）

- **思路**：用四个指针 `l`（左）、`r`（右）、`t`（上）、`b`（下）标记当前未填充的边界，每次按顺时针方向依次填充上边、右边、下边、左边，填充完一层后收缩对应边界，直到所有数字填完。
- **关键变量**：`l/r/t/b` 为四边界指针，`cur` 为当前要填入的数字。
- **复杂度**：O(n^2) 时间 | O(n^2) 空间（含返回矩阵）

### 解法二：方向向量模拟

- **思路**：预定义顺时针四个方向向量 `(0,1) (1,0) (0,-1) (-1,0)`，从 `(0,0)` 开始依次填入数字。每次计算下一步位置，如果碰到边界或已访问过的格子，就转向下一个方向。
- **关键变量**：`dirs` 为方向数组，`cur_d` 为当前方向索引，`(x, y)` 为当前位置，`(nx, ny)` 为试探的下一个位置。
- **复杂度**：O(n^2) 时间 | O(n^2) 空间（含返回矩阵）

---

## 解法对比

| 维度 | 解法一（四指针收缩） | 解法二（方向向量模拟） |
| :--- | :--- | :--- |
| 代码量 | 较长，需维护 4 个边界指针 | 更简洁，方向数组 + 转向逻辑 |
| 可扩展性 | 仅适用于正方形矩阵的填充 | 可推广到任意形状矩阵的螺旋遍历（如 54 题） |
| 转向逻辑 | 每条边写完后手动收缩对应边界 | 统一用 `cur_d = (cur_d + 1) % 4` 转向 |
| 易错点 | 四个边界的收缩顺序必须严格对应 | 边界条件判断要全面（越界 + 已访问） |

两种解法时间复杂度相同，**解法二（方向向量模拟）更简洁通用**，代码风格更一致，推荐作为首选写法。

## 代码

### 解法一：按层模拟（四指针收缩）

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        l, r, t, b = 0, n - 1, 0, n - 1
        cur = 1  # 当前要填的数字
        while cur <= n * n:
            for i in range(l, r + 1):
                matrix[t][i] = cur
                cur += 1
            t += 1  
            for i in range(t, b + 1):
                matrix[i][r] = cur
                cur += 1
            r -= 1 
            for i in range(r, l - 1, -1):
                matrix[b][i] = cur
                cur += 1
            b -= 1  
            for i in range(b, t - 1, -1):
                matrix[i][l] = cur
                cur += 1
            l += 1  
        return matrix
```

### 解法二：方向向量模拟

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  
        cur_d = 0    
        for i in range(1, n * n + 1):
            matrix[x][y] = i
            nx, ny = x + dirs[cur_d][0], y + dirs[cur_d][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
                cur_d = (cur_d + 1) % 4  
                nx, ny = x + dirs[cur_d][0], y + dirs[cur_d][1]
            x, y = nx, ny

        return matrix
```

---

## 易错点 / 边界细节

1. **转向条件必须同时检查越界和已访问**：`nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0`，缺一不可。
2. **如果使用解法一**，四个 for 循环必须严格按上→右→下→左顺序，且填完每条边后立即收缩对应指针。
3. **代码缺少 `from typing import List` 导入**：在 LeetCode 平台上可能自动处理，但本地运行会报 `NameError`。

---

## 关联题目

- [下一题推荐：303. 区域和检索 - 数组不可变](./303_range_sum_query_immutable.md) —— 前缀和入门，从矩阵模拟切换到区间求和场景。

---

## 源码文件

[源码](../Code/59.螺旋矩阵-ii.py)

---

## 一句话总结

方向向量带路走，撞墙右转不停步，由外向内填满图。