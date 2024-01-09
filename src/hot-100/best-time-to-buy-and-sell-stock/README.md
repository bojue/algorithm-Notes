
# 121. 买卖股票的最佳时机

## 分类

## 问题描述 

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

## 题解

```js
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let len = prices.length 
    let max = 0;
    let sub = Number.MAX_VALUE
    for(let i=0;i<len;i++) {
        let item = prices[i]
        sub = Math.min(sub, item)
        max = Math.max(max, item - sub)
    }
    return max
};
```