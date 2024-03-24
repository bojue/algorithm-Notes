
# 101. 对称二叉树

## 相关标签

- 树
- 深度优先搜索
- 广度优先搜索
- 二叉树

## 问题描述 

101. 对称二叉树 - 给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

示例 1：

[https://pic.leetcode.cn/1698026966-JDYPDU-image.png]


输入：root = [1,2,2,3,4,4,3]
输出：true


示例 2：

[https://pic.leetcode.cn/1698027008-nPFLbM-image.png]


输入：root = [1,2,2,null,3,null,3]
输出：false


 

提示：

 * 树中节点数目在范围 [1, 1000] 内
 * -100 <= Node.val <= 100

 

进阶：你可以运用递归和迭代两种方法解决这个问题吗？

## 题解


```ts
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    return isCheck(root, root)
};


var isCheck = function(p, q) {
    if(!p && !q) {
        return true
    } 
    if(!p || !q) {
        return false
    }

    return p.val === q.val && 
    isCheck(p.left, q.right) &&
    isCheck(q.left, p.right)
}
````