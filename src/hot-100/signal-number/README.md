# 136. 只出现一次的数字

## 分类

## 问题描述 


给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

 

示例 1 ：

输入：nums = [2,2,1]
输出：1
示例 2 ：

输入：nums = [4,1,2,1,2]
输出：4
示例 3 ：

输入：nums = [1]
输出：1
 

提示：

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
除了某个元素只出现一次以外，其余每个元素均出现两次。


## 题解

1. 方法一:异或

```TS
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let result = ''
    const len = nums.length

    for(let i=0;i<len;i++) {
        result = result ^ nums[i]
    }

    return result
};
```

2. 方法二:数组

```ts

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    for(let i=0;i<nums.length;i++) {
        const item = nums[i]
        if(nums.indexOf(item) === nums.lastIndexOf(item)) {
            return item
        }
    }
};

3. 方法二: Set集合
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    const newSet = new Set()
    const len = nums.length 

    for(let i=0;i<len;i++) {
        let item = nums[i]
        if(newSet.has(item)) {
            newSet.delete(item)
        } else {
            newSet.add(item)
        }
    }


    const iterator = newSet.values()
    return iterator.next().value
};

```