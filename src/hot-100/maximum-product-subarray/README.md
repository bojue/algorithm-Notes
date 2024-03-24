
# 152. 乘积最大子数组

## 相关标签

- 数组
- 动态规划

## 问题描述 

152. 乘积最大子数组 - 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

 

示例 1:


输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。


示例 2:


输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

 

提示:

 * 1 <= nums.length <= 2 * 104
 * -10 <= nums[i] <= 10
 * nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数

## 题解


```ts
function maxProduct(nums: number[]): number {
    let maxVal = nums[0]
    let minVal = nums[0]
    let result = maxVal
    for(let i=1;i<nums.length;i++) {
        let maxMiddleVal = maxVal || 1
        let minMiddleVal = minVal || 1
        let item = nums[i] 
        let data = [0, 0]
        if(item !== 0) {
             data = [
                Math.max(item * maxMiddleVal, item * minMiddleVal, item),
                Math.min(item * maxMiddleVal, item * minMiddleVal, item)
            ]
        }

        [maxVal, minVal] = data
        result = Math.max(result, maxVal)
    }
    return result
};
````