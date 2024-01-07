
# 234. 回文链表

## 分类

## 问题描述 

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    const list = []
    let temp = head

    while(temp) {
        list.push(temp.val)
        temp = temp.next
    }
    const len = list.length 
    for(let i=0;i<len;i++) {
        const isEqual = list[i] === list[len - 1 -i]
        if(!isEqual) {
            return false
        }
    }

    return true;
};
```