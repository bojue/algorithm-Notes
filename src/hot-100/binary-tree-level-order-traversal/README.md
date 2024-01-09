
# 102. 二叉树的层序遍历

## 分类

## 问题描述 

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。



示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
 

提示：

1 <= n <= 45

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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    let result = []
    if(!root) {
        return result
    }
    const queue = [root]
    while(queue.length) {
        let len = queue.length;
        let dataList = []
        for(let i=0;i<len;i++) {
            let item = queue.shift() 
            dataList.push(item.val)
            const {
                left,
                right
            } = item 
            if(left) {
                queue.push(left)
            }

            if(right) {
                queue.push(right)
            }
        }
        result.push(dataList)
    }


    return result
};
```