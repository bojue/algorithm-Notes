
# 2. 两数相加

## 相关标签

- 递归
- 链表
- 数学

## 问题描述 

2. 两数相加 - 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：

[https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg]


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.


示例 2：


输入：l1 = [0], l2 = [0]
输出：[0]


示例 3：


输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


 

提示：

 * 每个链表中的节点数在范围 [1, 100] 内
 * 0 <= Node.val <= 9
 * 题目数据保证列表表示的数字不含前导零

## 题解


```ts
/**
 * Definition for singly-linked list.
* function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let newHead = new ListNode(-1)
    let tempHead = newHead
    let temp = 0

    while(l1 || l2) {
        const v1 = l1?.val || 0
        const v2 = l2?.val || 0
        const curr = v1 + v2 + temp 
        const val = curr >= 10 ? curr -10 : curr
        temp = curr >= 10 ? 1 : 0
        newHead.next = new ListNode(val)

        if(l1) {
            l1 = l1.next
        }
        if(l2) {
            l2 = l2.next
        }
        newHead = newHead.next
    }

    if(temp) {
       newHead.next = new ListNode(temp) 
    }
   
    return tempHead.next 

};
````