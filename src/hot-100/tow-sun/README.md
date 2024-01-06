
# 1. 两数之和

## 分类

## 问题描述

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



## 题解

```ts
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const mapData = new Map()

    let len = nums.length 

    for(let i=0;i<len;i++) {
        let item = nums[i]
        let currentItem = target - item
        if(mapData.has(currentItem)) {
            return [i, mapData.get(currentItem)]
        } else {
            mapData.set(item,i)
        }
    }

    return []
};
```