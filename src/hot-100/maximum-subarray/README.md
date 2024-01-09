# 53. 最大子数组和

## 分类

## 问题描述 

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

## 题解

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let sum = 0
    let len = nums.length;
    let max = nums[0]
    for(let i=0;i<len;i++) {
        const currItem = nums[i]
        if(sum > 0) {
            sum = currItem + sum
        } else {
            sum = currItem
        }

        max = Math.max(sum, max)
    }

    return max
};
```