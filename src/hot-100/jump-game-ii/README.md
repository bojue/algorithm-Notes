
# 45. 跳跃游戏 II

## 相关标签

- 贪心
- 数组
- 动态规划

## 问题描述 

45. 跳跃游戏 II - 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

 * 0 <= j <= nums[i] 
 * i + j < n

返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

 

示例 1:


输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。


示例 2:


输入: nums = [2,3,0,1,4]
输出: 2


 

提示:

 * 1 <= nums.length <= 104
 * 0 <= nums[i] <= 1000
 * 题目保证可以到达 nums[n-1]

## 题解


```ts
function jump(nums: number[]): number {
    let len = nums.length
    let step = 0;
    let end = 0;
    let maxPositon = 0
    for(let i =0;i<len -1;i++) {
        maxPositon = Math.max(maxPositon, i + nums[i])
        if(i === end) {
            end = maxPositon
            step++
        }
    }

    return step
};
````