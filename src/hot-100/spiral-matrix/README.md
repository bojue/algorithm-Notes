
# 54. 螺旋矩阵

## 相关标签

- 数组
- 矩阵
- 模拟

## 问题描述 

54. 螺旋矩阵 - 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg]


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]


示例 2：

[https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg]


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


 

提示：

 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 10
 * -100 <= matrix[i][j] <= 100

## 题解


```ts
function spiralOrder(matrix: number[][]): number[] {
  const result =  []
  const rowLen = matrix.length 
  const colLen = matrix[0].length
  
  let len = rowLen * colLen
  let left =0;
  let top = 0;
  let right = colLen - 1
  let buttom = rowLen - 1

  while(result.length < len) {
    console.log('result', result.length , len)
    for(let i = left;i<=right;i++) {
        result.push(matrix[top][i])
    }
    top++
    for(let i = top;i<=buttom  && result.length < len;i++) {
        result.push(matrix[i][right])
    }
    right--
    for(let i = right;i >=left  && result.length < len;i--) {
        console.log(buttom, i, matrix[buttom], len)
        result.push(matrix[buttom][i])
    }
    buttom--
    for(let i = buttom;i >=top  && result.length < len;i--) {
        result.push(matrix[i][left])
    }
    left++
  }

  return result

};
````