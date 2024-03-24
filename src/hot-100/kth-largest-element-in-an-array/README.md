
# 215. 数组中的第K个最大元素

## 相关标签

- 数组
- 分治
- 快速选择
- 排序
- 堆（优先队列）

## 问题描述 

215. 数组中的第K个最大元素 - 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1:


输入: [3,2,1,5,6,4], k = 2
输出: 5


示例 2:


输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

 

提示：

 * 1 <= k <= nums.length <= 105
 * -104 <= nums[i] <= 104

## 题解


```ts
function findKthLargest(nums: number[], k: number): number {
  let res = 0

  function quickSort(nums, k) {
    if(!nums.length) {
        return 
    }

    const pivotIndex = nums.length >> 1;
    const pivot = nums[pivotIndex]

    const left = nums.filter(item => item < pivot)
    const mid = nums.filter(item => item == pivot)
    const right = nums.filter(item => item > pivot)

    const leftLen = left.length - 1
    const rightStartIndex = left.length + mid.length

    if(k <= leftLen) {
        quickSort(left, k)
    } else if(k > leftLen && k < rightStartIndex) {
        res = mid[0]  
    } else {
        quickSort(right, k - rightStartIndex)
    }


  }

  quickSort(nums, nums.length - k)
  return res;  
};
````