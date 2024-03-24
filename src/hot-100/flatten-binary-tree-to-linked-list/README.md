
# 114. 二叉树展开为链表

## 相关标签

- 栈
- 树
- 深度优先搜索
- 链表
- 二叉树

## 问题描述 

114. 二叉树展开为链表 - 给你二叉树的根结点 root ，请你将它展开为一个单链表：

 * 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
 * 展开后的单链表应该与二叉树 先序遍历 [https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin] 顺序相同。

 

示例 1：

[https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg]


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]


示例 2：


输入：root = []
输出：[]


示例 3：


输入：root = [0]
输出：[0]


 

提示：

 * 树中结点数在范围 [0, 2000] 内
 * -100 <= Node.val <= 100

 

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

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

/**
 Do not return anything, modify root in-place instead.
 */
function flatten(root: TreeNode | null): void {
    let newNode = null 
    helper(root)
    function helper(node: TreeNode | null) {
        if(!node) {
            return node
        }

        helper(node.right)
        helper(node.left)
        node.right = newNode
        node.left = null
        newNode = node
    }
    
};
````