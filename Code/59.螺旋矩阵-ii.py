#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
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
# @lc code=end

