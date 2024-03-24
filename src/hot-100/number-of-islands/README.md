
# 200. 岛屿数量

## 相关标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 矩阵

## 问题描述 

200. 岛屿数量 - 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：


输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1


示例 2：


输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3


 

提示：

 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 300
 * grid[i][j] 的值为 '0' 或 '1'

## 题解


```ts
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let count = 0;
    let row = grid.length 
    let col = grid[0].length 
    for(let i=0;i<row;i++) {
        for(let j=0;j<col;j++) {
            if(grid[i][j] === '1') {
                count++
                turnZero(i, j, grid)
            }
        }
    }
    return count
};

function turnZero(i, j, grid) {
    if( i < 0 || j < 0 || i>= grid.length || j >= grid[0].length || grid[i][j] === '0') {
        return 
    }

    grid[i][j] = '0'
    turnZero(i + 1, j,grid)
    turnZero(i -1, j, grid)
    turnZero(i, j+1, grid)
    turnZero(i, j-1, grid)

}
````