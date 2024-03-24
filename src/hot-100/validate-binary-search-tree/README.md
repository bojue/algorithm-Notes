
# 98. 验证二叉搜索树

## 相关标签

- 树
- 深度优先搜索
- 二叉搜索树
- 二叉树

## 问题描述 

98. 验证二叉搜索树 - 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

 * 节点的左子树只包含 小于 当前节点的数。
 * 节点的右子树只包含 大于 当前节点的数。
 * 所有左子树和右子树自身必须也是二叉搜索树。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg]


输入：root = [2,1,3]
输出：true


示例 2：

[https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg]


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。


 

提示：

 * 树中节点数目范围在[1, 104] 内
 * -231 <= Node.val <= 231 - 1

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

function isValidBST(root: TreeNode | null): boolean {
    if(!root) {
        return true
    }

    return helper(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER)
};

function helper(root: TreeNode | null, min: number, max: number) {
    if(!root ) {
        return true
    }

    if(root.val <= min || root.val >= max) {
        return false
    }

    return helper(root.left, min, root.val)
     && helper(root.right, root.val, max)
}
````