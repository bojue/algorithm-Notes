
# 169. 多数元素

## 相关标签

- 数组
- 哈希表
- 分治
- 计数
- 排序

## 问题描述 

169. 多数元素 - 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：


输入：nums = [3,2,3]
输出：3

示例 2：


输入：nums = [2,2,1,1,1,2,2]
输出：2


 

提示：
 * n == nums.length
 * 1 <= n <= 5 * 104
 * -109 <= nums[i] <= 109

 

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

## 题解


```ts
function majorityElement(nums: number[]): number {
    const map = new Map()
    let maxCount = 0;
    let max = 0

    for(let num of nums) {
        const curr = (map.get(num) || 0) + 1
        map.set(num, curr)
        maxCount = Math.max(curr, maxCount)
        if(maxCount === curr) {
            max = num
        }

    }

    

    return  max
};
````