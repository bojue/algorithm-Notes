
# 230. 二叉搜索树中第K小的元素

## 相关标签

- 树
- 深度优先搜索
- 二叉搜索树
- 二叉树

## 问题描述 

230. 二叉搜索树中第K小的元素 - 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

 

示例 1：

[https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg]


输入：root = [3,1,4,null,2], k = 1
输出：1


示例 2：

[https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg]


输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3


 

 

提示：

 * 树中的节点数为 n 。
 * 1 <= k <= n <= 104
 * 0 <= Node.val <= 104

 

进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？

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
function kthSmallest(root: TreeNode | null, k: number): number {
    const stack = []
    while(root !=  null || stack.length)  {
        while(root != null) {
            stack.push(root)
            root = root.left
        }
        root = stack.pop()
        k--;
        if(!k) {
            break
        }
        root = root.right
    }
    return root.val
};
````