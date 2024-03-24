
# 105. 从前序与中序遍历序列构造二叉树

## 相关标签

- 树
- 数组
- 哈希表
- 分治
- 二叉树

## 问题描述 

105. 从前序与中序遍历序列构造二叉树 - 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

 

示例 1:

[https://assets.leetcode.com/uploads/2021/02/19/tree.jpg]


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]


示例 2:


输入: preorder = [-1], inorder = [-1]
输出: [-1]


 

提示:

 * 1 <= preorder.length <= 3000
 * inorder.length == preorder.length
 * -3000 <= preorder[i], inorder[i] <= 3000
 * preorder 和 inorder 均 无重复 元素
 * inorder 均出现在 preorder
 * preorder 保证 为二叉树的前序遍历序列
 * inorder 保证 为二叉树的中序遍历序列

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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    if(!preorder.length ) {
        return null
    }
    const head = preorder[0]
    const root = new TreeNode(head)
    const index = inorder.findIndex(item => item === head)
    root.left  = buildTree(preorder.slice(1, index + 1), inorder.slice(0, index))
    root.right = buildTree(preorder.slice(index+1), inorder.slice(index + 1))

    return root
};
````