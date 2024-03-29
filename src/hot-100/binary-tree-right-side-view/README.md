
# 199. 二叉树的右视图

## 相关标签

- 树
- 深度优先搜索
- 广度优先搜索
- 二叉树

## 问题描述 

199. 二叉树的右视图 - 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

示例 1:

[https://assets.leetcode.com/uploads/2021/02/14/tree.jpg]


输入: [1,2,3,null,5,null,4]
输出: [1,3,4]


示例 2:


输入: [1,null,3]
输出: [1,3]


示例 3:


输入: []
输出: []


 

提示:

 * 二叉树的节点个数的范围是 [0,100]
 * -100 <= Node.val <= 100 

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
 * @return {number[]}
 */
var rightSideView = function(root) {
    if(!root) {
        return []
    }

    const result = []
    const queue = [root] 

    while(queue.length) {
        const len = queue.length 
        const levelList = []
        for(let i=0;i<len;i++) {
            const item = queue.shift()
            const {
                val, 
                left, 
                right
            } = item
            levelList.push(val)

            if(left) {
                queue.push(left)
            }

            if(right) {
                queue.push(right)
            }
 
        }
        result.push(levelList)
    }
    return result.map(item => item.pop())
};
````