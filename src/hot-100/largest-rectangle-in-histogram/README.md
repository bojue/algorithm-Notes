
# 84. 柱状图中最大的矩形

## 相关标签

- 栈
- 数组
- 单调栈

## 问题描述 

84. 柱状图中最大的矩形 - 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

示例 1:

[https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg]


输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10


示例 2：

[https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg]


输入： heights = [2,4]
输出： 4

 

提示：

 * 1 <= heights.length <=105
 * 0 <= heights[i] <= 104

## 题解


```ts
function largestRectangleArea(heights: number[]): number {
    let len = heights.length 
    let stack = []
    let max = 0

    for(let i=0;i<=len;i++) {
        while(stack.length && (i==len || heights[stack[stack.length -1]] > heights[i])) {
            const height = heights[stack.pop()]
            const width = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
            max = Math.max(max, width * height)
        }
        stack.push(i)
    }

    return max
};
````