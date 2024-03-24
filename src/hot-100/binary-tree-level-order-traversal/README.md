
# 102. 二叉树的层序遍历

## 相关标签

- 树
- 广度优先搜索
- 二叉树

## 问题描述 

102. 二叉树的层序遍历 - 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

 

示例 1：

[https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg]


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]


示例 2：


输入：root = [1]
输出：[[1]]


示例 3：


输入：root = []
输出：[]


 

提示：

 * 树中节点数目在范围 [0, 2000] 内
 * -1000 <= Node.val <= 1000

## 题解


```ts


var levelOrder = function(root) {
    const result = []
    if(!root) {
        return result
    }
    const queue = [root]
    console.log('queue', queue)

    while(queue.length) {
        console.log(queue)
        let level_list = []
        const len = queue.length 
        for(let i=0;i<len;i++) {
            const curr =  queue.shift()
            if(curr) {
                const {
                    val,
                    left,
                    right
                } = curr

                level_list.push(val)
                if(left) {
                    queue.push(left)
                } 
                if(right) {
                    queue.push(right)
                }
            }
        }
        result.push(level_list)
    }

    return result
};
````