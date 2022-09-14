## 22. 括号生成

### 问题描述

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 
### 思路

相对于暴力遍历的解题思路，这道题目通过判断`（`和`）`的条件，采用回溯法完成：

1. n对`()`组成字符串`str`,也就是`(`的最大数目和`)`最大数目都是n
2. `(`个数小于n,则`str`可以拼接`(`
3. `(`个数大于`)`的个数，则`str`可以拼接`)`
4. 当两边个数都是n则数据合法，返回结果

### 题解

```ts
function generateParenthesis(n: number): string[] {
    let result = []
    const dfs = function(left: number, right: number, str: string){
        if(left === n && right === n) {
           return  result.push(str)
        } 
        if(left < n) {
            dfs(left+1, right, str + '(')
        } 
        if(left > right) {
            dfs(left, right+1, str + ')')
        }
    }   

    dfs(0, 0, '')
    return result
};

```