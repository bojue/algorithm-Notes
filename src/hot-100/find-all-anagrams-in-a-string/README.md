
# 438. 找到字符串中所有字母异位词

## 分类

## 问题描述 

438. 找到字符串中所有字母异位词 - 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

 

示例 1:


输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。


 示例 2:


输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


 

提示:

 * 1 <= s.length, p.length <= 3 * 104
 * s 和 p 仅包含小写字母

## 题解

```js
function findAnagrams(s: string, p: string): number[] {
    let sLen = s?.length 
    let pLen = p?.length
    const result = []
    if(sLen < pLen) {
        return []
    }
    const sCountList = new Array(26).fill(0)
    const pCountList = new Array(26).fill(0)

    for(let i=0;i<pLen;i++) {
        ++sCountList[s[i]?.charCodeAt(0) - 'a'.charCodeAt(0)]
        ++pCountList[p[i]?.charCodeAt(0) - 'a'.charCodeAt(0)]
    }

    if(sCountList.toString() === pCountList.toString()) {
        result.push(0)
    }

    let len = sLen - pLen
    for(let i=0;i<len;i++) {
        --sCountList[s[i].charCodeAt(0) - 'a'.charCodeAt(0)]
        ++sCountList[s[i+pLen].charCodeAt(0) - 'a'.charCodeAt(0)]
        if(sCountList.toString() === pCountList.toString()) {
            result.push(i+1)
        }
    }

    return result
};
```