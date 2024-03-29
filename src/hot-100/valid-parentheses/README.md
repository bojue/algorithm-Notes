
# 20. 有效的括号

## 相关标签

- 栈
- 字符串

## 问题描述 

20. 有效的括号 - 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

 1. 左括号必须用相同类型的右括号闭合。
 2. 左括号必须以正确的顺序闭合。
 3. 每个右括号都有一个对应的相同类型的左括号。

 

示例 1：


输入：s = "()"
输出：true


示例 2：


输入：s = "()[]{}"
输出：true


示例 3：


输入：s = "(]"
输出：false


 

提示：

 * 1 <= s.length <= 104
 * s 仅由括号 '()[]{}' 组成

## 题解


```ts
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let listData = s.split('')
    let len = listData.length 
    let list = []
    let dataMap = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    if(len % 2) {
        return false
    }

    for(let i=0;i<len;i++) {
        let item = listData[i]
        const isLeft = !dataMap[item]
        if(isLeft) {
            list.push(item)
        } else {
            const last = list.pop()
            if(dataMap[item] !== last) {
                return false
            } 
        }
    }


    return !list.length
};
````