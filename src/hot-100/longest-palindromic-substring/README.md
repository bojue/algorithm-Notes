
# 5. 最长回文子串

## 相关标签

- 字符串
- 动态规划

## 问题描述 

5. 最长回文子串 - 给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

 

示例 1：


输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。


示例 2：


输入：s = "cbbd"
输出："bb"


 

提示：

 * 1 <= s.length <= 1000
 * s 仅由数字和英文字母组成

## 题解


```ts
function longestPalindrome(s: string): string {
    let res = ''

    const len = s.length 

    for(let i=0;i<len;i++) {
        const s1 = palindromeHandler(s, i, i) 
        const s2 =  palindromeHandler(s, i, i+1)

        res = res.length > s1.length ? res : s1
        res = res.length > s2.length ? res: s2;
    }    

    return res
};

function palindromeHandler(str: string ,left: number, right: number) {
    while(left >= 0 && right < str.length && str[left] === str[right]) {
        left--
        right++
    }

    return str.substr(left+1, right - left -1)
}



````