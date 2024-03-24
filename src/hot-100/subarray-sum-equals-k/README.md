
# 560. 和为 K 的子数组

## 相关标签

- 数组
- 哈希表
- 前缀和

## 问题描述 

560. 和为 K 的子数组 - 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

 

示例 1：


输入：nums = [1,1,1], k = 2
输出：2


示例 2：


输入：nums = [1,2,3], k = 3
输出：2


 

提示：

 * 1 <= nums.length <= 2 * 104
 * -1000 <= nums[i] <= 1000
 * -107 <= k <= 107

## 题解


```ts
function subarraySum(nums: number[], k: number): number {
    const map = new Map()
    map.set(0, 1)
    let pre = 0
    let count = 0

    for(let i=0;i<nums.length;i++) {
        pre +=  nums[i]

        if(map.has(pre -k)) {
            count += map.get(pre -k)
        }
        map.set(pre,  map.has(pre)? map.get(pre) + 1 : 1)
    }

    return count
};
````