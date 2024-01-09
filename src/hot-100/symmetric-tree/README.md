
# 101. 对称二叉树

## 分类

## 问题描述
给你一个二叉树的根节点 root ， 检查它是否轴对称。


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
```