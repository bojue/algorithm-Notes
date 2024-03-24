
# 94. 二叉树的中序遍历

## 相关标签

- 栈
- 树
- 深度优先搜索
- 二叉树

## 问题描述 

94. 二叉树的中序遍历 - 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg]


输入：root = [1,null,2,3]
输出：[1,3,2]


示例 2：


输入：root = []
输出：[]


示例 3：


输入：root = [1]
输出：[1]


 

提示：

 * 树中节点数目在范围 [0, 100] 内
 * -100 <= Node.val <= 100

 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

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

function inorderTraversal(root: TreeNode | null): number[] {
    const result = []
    preorder(root, result)
    return result
};

function preorder(root, result) {
    if(!root) return
    preorder(root.left, result)
    result.push(root.val)
    preorder(root.right, result)
}
````