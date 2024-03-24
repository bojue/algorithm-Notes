
# 22. 括号生成

## 相关标签

- 字符串
- 动态规划
- 回溯

## 问题描述 

22. 括号生成 - 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：


输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]


示例 2：


输入：n = 1
输出：["()"]


 

提示：

 * 1 <= n <= 8

## 题解


```ts
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {

    const result = []
    
    const def = (left, right, str) => {
        const len = str?.length

        if(len === 2 * n) {
            result.push(str)
        }

        if(left > 0) {
            def(left -1, right, str + '(')
        }  
        if(right > left) {
            def(left, right -1, str + ')')
        }

    }

    def(n , n, '')
    return result
};
````