# 55. 跳跃游戏

## 分类

## 问题描述 
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。



## 题解

```js
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    const len = nums.length 
    let end = len - 1
    for(let i= len -1;i>= 0;i-- ) {
        if((end - i )<= nums[i]) {
            end = i
        } 
    }
    return !end
};
```