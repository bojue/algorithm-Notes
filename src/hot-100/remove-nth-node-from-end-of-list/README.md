# 19. 删除链表的倒数第 N 个结点

## 分类

## 问题描述 

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

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
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let fastHead = head 
    let slowHead = head 

    while(n--) {
        fastHead = fastHead.next
    }

    if(!fastHead) {
        return head.next
    }

    while(fastHead.next) {
        fastHead = fastHead.next 
        slowHead = slowHead.next
    }
    slowHead.next = slowHead.next.next
    return head
};
```