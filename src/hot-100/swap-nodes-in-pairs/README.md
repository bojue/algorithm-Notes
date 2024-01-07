
# 24. 两两交换链表中的节点

## 分类

## 问题描述 

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

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
 * @return {ListNode}
 */
var swapPairs = function(head) {
    if(!head?.next) {
        return head
    }
    let newHead = head.next 
    head.next = swapPairs(newHead.next) 
    newHead.next = head
    return newHead;
};
```