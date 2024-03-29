
# 75. 颜色分类

## 相关标签

- 数组
- 双指针
- 排序

## 问题描述 

75. 颜色分类 - 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 [https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95]对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

 

示例 1：


输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]


示例 2：


输入：nums = [2,0,1]
输出：[0,1,2]


 

提示：

 * n == nums.length
 * 1 <= n <= 300
 * nums[i] 为 0、1 或 2

 

进阶：

 * 你能想出一个仅使用常数空间的一趟扫描算法吗？

## 题解


```ts
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    const len = nums.length
    let curr = 0;
    let right = len -1
    let tempIndex = 0

    const swap = function(a, b) {
        const temp = nums[b]
        nums[b] = nums[a]
        nums[a] = temp
    }
    while(curr <= right) {
        const item = nums[curr]
        if(item === 0) {
            swap(curr, tempIndex)
            curr++
            tempIndex++
        } else if(item === 2) {
            swap(curr, right)
            right--
        } else {
            curr++
        }
    }
};
````