
# 25. K 个一组翻转链表

## 相关标签

- 递归
- 链表

## 问题描述 

25. K 个一组翻转链表 - 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg]


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]


示例 2：

[https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg]


输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]


 

提示：
 * 链表中的节点数目为 n
 * 1 <= k <= n <= 5000
 * 0 <= Node.val <= 1000

 

进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？

## 题解


```ts
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    let curr = head;
    let count = 0;
    while( curr !== null  && count !== k) {
        curr = curr.next
        count++
    }
    if(count !== k) {
        return head;
    }

    let newHead = reverseKGroup(curr, k)

    while(count> 0) {
        const next = head.next 
        head.next = newHead
        newHead = head 
        head = next
        count--
    }
    return newHead

};
````