
# 74. 搜索二维矩阵

## 分类

## 问题描述 

74. 搜索二维矩阵 - 给你一个满足下述两条属性的 m x n 整数矩阵：

 * 每行中的整数从左到右按非严格递增顺序排列。
 * 每行的第一个整数大于前一行的最后一个整数。

给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/10/05/mat.jpg]


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true


示例 2：

[https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg]


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false


 

提示：

 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 100
 * -104 <= matrix[i][j], target <= 104

## 题解

