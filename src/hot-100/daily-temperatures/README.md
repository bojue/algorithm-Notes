
# 739. 每日温度

## 相关标签

- 栈
- 数组
- 单调栈

## 问题描述 

739. 每日温度 - 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

 

示例 1:


输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]


示例 2:


输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]


示例 3:


输入: temperatures = [30,60,90]
输出: [1,1,0]

 

提示：

 * 1 <= temperatures.length <= 105
 * 30 <= temperatures[i] <= 100

## 题解


```ts
/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    let len = temperatures.length
    let stack = []
    const res = new Array(len).fill(0)
    for(let i = len-1;i>=0;i--) {
        const item = temperatures[i]
        while(stack.length && item >= temperatures[stack[stack.length-1]]) {
            stack.pop();
        }

        if(stack.length){
            res[i] = stack[stack.length -1] -i
        }
        
        stack.push(i)
    }

    return res
};
````