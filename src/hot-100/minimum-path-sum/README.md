
# 64. 最小路径和

## 相关标签

- 数组
- 动态规划
- 矩阵

## 问题描述 

64. 最小路径和 - 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg]


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。


示例 2：


输入：grid = [[1,2,3],[4,5,6]]
输出：12


 

提示：

 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 200
 * 0 <= grid[i][j] <= 200

## 题解


```ts
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
   let result = Number.MAX;
   let rowLen = grid.length 
   let colLen = grid[0].length 

   for(let i=0;i<rowLen;i++) {
       for(let j=0;j<colLen;j++) {
           if(!i && !j) {
               continue
           }
           if(i === 0) {
              grid[i][j] += grid[i][j-1]
           } else if(j === 0) {
              grid[i][j] += grid[i-1][j]
           } else {
                grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]) 
           }
          
       }
   }

   return  grid[rowLen -1][colLen -1] 
};
````