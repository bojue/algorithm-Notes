# 21. 合并两个有序链表

## 分类

## 问题描述 

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 


## 题解

1. 方法一:摩尔投屏

```TS
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let newHead = new ListNode(-1)
    let temp = newHead
    while(list1 && list2) {
        const v1 = list1.val 
        const v2 = list2.val 

        if(v1 < v2) {
            newHead.next = new ListNode(v1) 
            list1 = list1.next
        } else {
            newHead.next = new ListNode(v2) 
            list2 = list2.next
        }

        newHead = newHead.next
    }
    newHead.next = list1 || list2
    return temp.next
};
```