# 64. 最小路径和

## 分类

## 问题描述 
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。



## 题解

```js
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
```