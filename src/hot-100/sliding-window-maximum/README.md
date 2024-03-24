
# 239. 滑动窗口最大值

## 相关标签

- 队列
- 数组
- 滑动窗口
- 单调队列
- 堆（优先队列）

## 问题描述 

239. 滑动窗口最大值 - 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

 

示例 1：


输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


示例 2：


输入：nums = [1], k = 1
输出：[1]


 

提示：

 * 1 <= nums.length <= 105
 * -104 <= nums[i] <= 104
 * 1 <= k <= nums.length

## 题解


```ts
function maxSlidingWindow(nums: number[], k: number): number[] {
    let result = []
    let queue = []

    let len = nums.length 

    for(let i=0;i<len;i++) {
        // 移除窗口外的数据
        while(queue.length && queue[0] === i -k) {
            queue.shift()
        }

        while(queue.length && nums[ queue[queue.length - 1] ]< nums[i]) {
            queue.pop()
        }

        queue.push(i)

        if(i >= k -1) {
            result.push(nums[queue[0]])
        }
    }

    return result
};
````