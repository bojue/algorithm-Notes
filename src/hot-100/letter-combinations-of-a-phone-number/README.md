
# 17. 电话号码的字母组合

## 相关标签

- 哈希表
- 字符串
- 回溯

## 问题描述 

17. 电话号码的字母组合 - 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

[https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/11/09/200px-telephone-keypad2svg.png]

 

示例 1：


输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]


示例 2：


输入：digits = ""
输出：[]


示例 3：


输入：digits = "2"
输出：["a","b","c"]


 

提示：

 * 0 <= digits.length <= 4
 * digits[i] 是范围 ['2', '9'] 的一个数字。

## 题解


```ts
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const len = digits.length 
    const result = []
    if(!len) {
        return result
    }
    const digitsData = digits.split('')
    const dataMap = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',   '7': 'pqrs', '8': 'tuv', '9': 'wxyz' };


    const dfs = function(str, i) {
        if(i > len -1) {
            result.push(str)
            return
        }
        let strData =  dataMap[digitsData[i]]?.split('')
        if(!strData) {
            return
        }
        let subLen = strData.length

        for(let j=0;j <subLen;j++) {
            dfs(str + strData[j], i+1)
        }

    }

    dfs('', 0)

    return result
};
````