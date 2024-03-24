
# 3. 无重复字符的最长子串

## 相关标签

- 哈希表
- 字符串
- 滑动窗口

## 问题描述 

3. 无重复字符的最长子串 - 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:


输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


示例 2:


输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。


示例 3:


输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


 

提示：

 * 0 <= s.length <= 5 * 104
 * s 由英文字母、数字、符号和空格组成

## 题解


```ts
function lengthOfLongestSubstring(s: string): number {
    let len = s?.length 
    if(!len) {
        return 0
    }
    let str = ''
    let max = 1

    for(let i=0;i<len;i++) {
        let curr = s.charAt(i)
        while(str.indexOf(curr) > -1) {
            str = str.substring(1)
        }
        str = str + curr
        max = Math.max(max, str.length)
    }

    return max
};  
````