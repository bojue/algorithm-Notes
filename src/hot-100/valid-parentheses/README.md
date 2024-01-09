
# 20. 有效的括号

## 分类

## 问题描述
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。



## 题解

```ts
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const list = s.split('')
    const len = list.length 
    const stack = []

    if(len % 2) {
        return false
    }

    for(let i=0;i<len;i++) {
        let item = list[i]
        const _isLeft = ['(', '[', '{'].indexOf(item) > -1
        if(_isLeft) {
            stack.push(item)
        } else {
            const pre = stack[stack.length -1]
            const isRight = ')' === item && pre === '(' ||
                ']' === item && pre === '[' ||
                '}' === item && pre === '{'
            if(isRight) {
                stack.pop()
            } else {
                return false
            }

        }
    }
    return stack.length === 0
};
```