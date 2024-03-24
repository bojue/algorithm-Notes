
# 41. 缺失的第一个正数

## 相关标签

- 数组
- 哈希表

## 问题描述 

41. 缺失的第一个正数 - 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

 

示例 1：


输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。

示例 2：


输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。

示例 3：


输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。

 

提示：

 * 1 <= nums.length <= 105
 * -231 <= nums[i] <= 231 - 1

## 题解


```ts
function firstMissingPositive(nums: number[]): number {
    const len = nums.length
    let result = nums.length + 1

    if(nums.indexOf(1) === -1) {
        return 1
    }
    for(let i=0;i<len;i++) {
        if(nums[i] <=0) {
            nums[i] = 1
        }
    }

    console.log(nums)

    for(let i=0;i<len;i++) {
        const num = Math.abs(nums[i])
        if (num <= len) {
            nums[num - 1] = -Math.abs(nums[num-1])
        }
    }

    console.log(nums)

    for(let i=0;i<len;i++) {
        const item = nums[i]
        if(item > 0) {
            return i + 1
        }
    }

    return result
};
````