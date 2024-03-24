
# 4. 寻找两个正序数组的中位数

## 相关标签

- 数组
- 二分查找
- 分治

## 问题描述 

4. 寻找两个正序数组的中位数 - 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：


输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2


示例 2：


输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5


 

 

提示：

 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -106 <= nums1[i], nums2[i] <= 106

## 题解


```ts
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let len1 = nums1.length 
    let len2 = nums2.length 
    let len = len1 + len2
    let nums = []
    let curr = 0;
    let i = 0;
    let j = 0;

    while(curr !== len) {
        if(i === len1) {
            while(j != len2) {
                nums[curr++] = nums2[j++]
            }

            break;
        }

        if(j === len2) {
            while(i != len1) {
                nums[curr++] = nums1[i++]
            }
            break;
        }

    
        if(nums1[i] > nums2[j]) {
            nums[curr++] = nums2[j++]
        } else {
            nums[curr++] = nums1[i++]
        }
    }

    const data = curr % 2 != 0 ? nums[(curr-1)/2]: ((nums[curr/2 -1] + nums[curr /2 ]) / 2.0)  
    return data
};
````