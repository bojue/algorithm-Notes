
# 118. 杨辉三角

## 相关标签

- 数组
- 动态规划

## 问题描述 

118. 杨辉三角 - 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

[https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif]

 

示例 1:


输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


示例 2:


输入: numRows = 1
输出: [[1]]


 

提示:

 * 1 <= numRows <= 30

## 题解


```ts
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    const result = []

    for(let i=0;i<numRows;i++) {
        result[i] = Array(i+1).fill(1)
        for(let j=1;j<i;j++) {
            result[i][j] = result[i-1][j] + result[i-1][j-1]
        }
    }

    return result
};
````