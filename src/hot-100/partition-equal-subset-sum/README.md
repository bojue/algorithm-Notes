
# 416. 分割等和子集

## 相关标签

- 数组
- 动态规划

## 问题描述 

416. 分割等和子集 - 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

示例 1：


输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：


输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


 

提示：

 * 1 <= nums.length <= 200
 * 1 <= nums[i] <= 100

## 题解


```ts
function canPartition(nums: number[]): boolean {
    const sum = nums.reduce((a, b) => a + b, 0)
    if(sum % 2 === 1) {
        return false
    }

    const target = sum / 2
    const dp = new Array(target+1).fill(false)
    const len = nums.length 
    for(let i=0;i<=len;i++) {
        for(let j=target;j>=0;j--) {
            if(j - nums[i] >= 0) {
                dp[j] = Math.max(dp[j], dp[j - nums[i]] + nums[i])
            }
        }
    }
    return dp[target] === target
};
````