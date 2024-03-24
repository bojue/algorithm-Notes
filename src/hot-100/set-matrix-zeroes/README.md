
# 73. 矩阵置零

## 相关标签

- 数组
- 哈希表
- 矩阵

## 问题描述 

73. 矩阵置零 - 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 [http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95] 算法。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg]


输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]


示例 2：

[https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg]


输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]


 

提示：

 * m == matrix.length
 * n == matrix[0].length
 * 1 <= m, n <= 200
 * -231 <= matrix[i][j] <= 231 - 1

 

进阶：

 * 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
 * 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
 * 你能想出一个仅使用常量空间的解决方案吗？

## 题解


```ts
/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    let rowNum = matrix.length
    let colNum = matrix[0].length
    let rowArray = new Array(colNum).fill(false)
    let colArray = new Array(colNum).fill(false)
    for(let i=0; i< rowNum;i++) {
        for(let j=0;j<colNum;j++) {
            if(matrix[i][j]=== 0) {
                rowArray[i] = true
                colArray[j] = true
            }
        }
    }


    for(let i=0; i< rowNum;i++) {
        for(let j=0;j<colNum;j++) {
            if(rowArray[i] || colArray[j]){
                matrix[i][j] = 0
            }
        }
    }
};
````