
# 21. 合并两个有序链表

## 相关标签

- 递归
- 链表

## 问题描述 

21. 合并两个有序链表 - 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：

[https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg]


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]


示例 2：


输入：l1 = [], l2 = []
输出：[]


示例 3：


输入：l1 = [], l2 = [0]
输出：[0]


 

提示：

 * 两个链表的节点数目范围是 [0, 50]
 * -100 <= Node.val <= 100
 * l1 和 l2 均按 非递减顺序 排列

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
````