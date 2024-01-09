
# 543. 二叉树的直径

## 分类

## 问题描述 

给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。
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
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    if(!root) return 0
    let result = 0

    function def(root) {
        if(!root) {
            return 0
        }
        const left = def(root.left)
        const right = def(root.right)

        result = Math.max(result, (left + right))
        return Math.max(left, right) + 1
    }

    def(root)
    return result
};
```