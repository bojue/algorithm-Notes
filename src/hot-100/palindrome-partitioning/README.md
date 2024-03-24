
# 131. 分割回文串

## 相关标签

- 字符串
- 动态规划
- 回溯

## 问题描述 

131. 分割回文串 - 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

 

示例 1：


输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]


示例 2：


输入：s = "a"
输出：[["a"]]


 

提示：

 * 1 <= s.length <= 16
 * s 仅由小写英文字母组成

## 题解


```ts
function partition(s: string): string[][] {
    const result:string[][]  = []
    const current = []
    backtrack(0, s, current, result);
    return result 
};

function backtrack(start: number, s: string, current: string[], result:string[][] ) {
    if(start === s.length ) {
        result.push([...current])
        return 
    }

    for(let i= start;i<s.length;i++) {
        const str = s.substring(start, i+1)
        if(isPalindrome(str)) {
            current.push(str)
            backtrack(i+1, s, current, result)
            current.pop()
        }
    }
}

function isPalindrome(s: string) {
    let left = 0;
    let right = s.length -1 
    while(left < right) {
        if(s[left] !== s[right]) {
            return false
        }

        left++
        right--
    }
    return true
}
````