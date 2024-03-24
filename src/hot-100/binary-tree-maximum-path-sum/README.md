
# 124. 二叉树中的最大路径和

## 相关标签

- 树
- 深度优先搜索
- 动态规划
- 二叉树

## 问题描述 

124. 二叉树中的最大路径和 - 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg]


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：

[https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg]


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


 

提示：

 * 树中节点数目范围是 [1, 3 * 104]
 * -1000 <= Node.val <= 1000

## 题解


```ts
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxPathSum(root: TreeNode | null): number {
    let maxVal = -Infinity

    function maxPathSumHelper(node) {
        if(!node) {
            return 0
        }
        const leftSum = maxPathSumHelper(node?.left)
        const rightSum = maxPathSumHelper(node?.right)
        maxVal = Math.max(
            maxVal,
            node.val,
            leftSum + node.val,
            leftSum + node.val + rightSum,
            rightSum + node.val)

        return Math.max(leftSum + node.val , rightSum + node.val, node.val)
    }

    maxPathSumHelper(root)

    return maxVal
};  
````