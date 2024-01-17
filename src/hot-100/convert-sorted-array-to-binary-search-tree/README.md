
# 108. 将有序数组转换为二叉搜索树

## 分类

## 问题描述 

108. 将有序数组转换为二叉搜索树 - 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

 

示例 1：

[https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg]


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
[https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg]


示例 2：

[https://assets.leetcode.com/uploads/2021/02/18/btree.jpg]


输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。


 

提示：

 * 1 <= nums.length <= 104
 * -104 <= nums[i] <= 104
 * nums 按 严格递增 顺序排列

## 题解

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    const root = new TreeNode(null)
    const len = nums.length 
    if(len) {
        const mid = len / 2
        root.left = sortedArrayToBST(nums.splice(0, mid))
        root.val = nums[0]
        root.right = sortedArrayToBST(nums.splice(1))
    } else {
        return null
    }

    return root
};

```