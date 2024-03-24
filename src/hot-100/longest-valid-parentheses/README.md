
# 32. 最长有效括号

## 相关标签

- 栈
- 字符串
- 动态规划

## 问题描述 

32. 最长有效括号 - 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：


输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"


示例 2：


输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"


示例 3：


输入：s = ""
输出：0


 

提示：

 * 0 <= s.length <= 3 * 104
 * s[i] 为 '(' 或 ')'

## 题解


```ts
function longestValidParentheses(s: string): number {
    const stack = []
    let start = -1
    let maxVal = 0
    let len = s.length;

    for(let i=0;i<len;i++) {
        let item = s[i]
        if(item === '(') {
            stack.push(i)
        } else {
            if(stack.length === 0) {
                start = i
            } else {
                stack.pop()
                if(stack.length === 0) {
                    maxVal = Math.max(maxVal,  i - start)
                } else {
                    maxVal = Math.max(maxVal, i - stack[stack.length -1])
                }
            }
        }
    }

    return maxVal


};
````