
# 11. 盛最多水的容器

## 分类

## 问题描述 

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

## 题解

```js
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    const len = height.length 
    let i=0;
    let j= len -1 
    let max = 0

    while(i<j) {
        if(height[i] > height[j]) {
            max = Math.max(max, height[j] * (j - i))
            j--
        } else {
            max = Math.max(max,height[i] * (j - i))
            i++
        }
    }

    return max
};
```