
# 42. 接雨水

## 相关标签

- 栈
- 数组
- 双指针
- 动态规划
- 单调栈

## 问题描述 

42. 接雨水 - 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：

[https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png]


输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 


示例 2：


输入：height = [4,2,0,3,2,5]
输出：9


 

提示：

 * n == height.length
 * 1 <= n <= 2 * 104
 * 0 <= height[i] <= 105

## 题解


```ts
function trap(height: number[]): number {
    let res = 0
    let len = height.length - 1

    if(len <= 1) {
        return res
    }
    
    let left = 0;
    let right = len 
    let maxLeft = 0
    let maxRight = 0;
    while(left < right) {
        maxLeft = Math.max(maxLeft, height[left])
        maxRight = Math.max(maxRight, height[right])
        if(height[left] < height[right]) {
            res += maxLeft - height[left]
            left++
        } else {
            res += maxRight - height[right]
            right--
        }
    }

    return res
};
````