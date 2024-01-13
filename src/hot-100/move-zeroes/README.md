# 283. 移动零

## 分类

## 问题描述 
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

## 题解

```js
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    const len = nums.length
    let left = 0
    let right = 0
    while(right < len) {
        const curr = nums[right] 
        if(curr) {
            const temp = nums[left]
            nums[left] = curr
            nums[right] = temp
            left++
        }
        right++
    }
};
```