
# 46. 全排列

## 相关标签

- 数组
- 回溯

## 问题描述 

46. 全排列 - 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：


输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


示例 2：


输入：nums = [0,1]
输出：[[0,1],[1,0]]


示例 3：


输入：nums = [1]
输出：[[1]]


 

提示：

 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * nums 中的所有整数 互不相同

## 题解


```ts
function permute(nums: number[]): number[][] {
    const result: number[][] = []
    bracktrack(nums, [], result)
    return result
    
};

function bracktrack(nums: number[], current: number[], result: number[][]) {
    if(current.length === nums.length) {
        result.push([...current])
        return 
    }

    for(let i=0;i<nums.length;i++) {
        if(current.includes(nums[i])) {
            continue;
        }
        current.push(nums[i])
        bracktrack(nums, current, result)
        current.pop()
    
    }

}
````