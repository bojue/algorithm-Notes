
# 148. 排序链表

## 相关标签

- 链表
- 双指针
- 分治
- 排序
- 归并排序

## 问题描述 

148. 排序链表 - 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

 

示例 1：

[https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg]


输入：head = [4,2,1,3]
输出：[1,2,3,4]


示例 2：

[https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg]


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]


示例 3：


输入：head = []
输出：[]


 

提示：

 * 链表中节点的数目在范围 [0, 5 * 104] 内
 * -105 <= Node.val <= 105

 

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

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

function sortList(head: ListNode | null): ListNode | null {
    return toSortList(head, null)
};

function toSortList(head, tail) {
    if(head === null){
        return head
    }

    if(head?.next === tail) {
        head.next = null
        return head
    }

    let slow = head;
    let fast = head;

    while(fast !== tail) {
        slow = slow.next
        fast = fast.next 
        if(fast !== tail) {
            fast = fast.next
        }
    }

    const mid = slow 
    return merge(toSortList(head, mid), toSortList(mid, tail))
}

function merge(head1, head2) {
    const head = new ListNode(0)
    let temp = head
    let temp1 = head1 
    let temp2 = head2 

    while(temp1 !== null && temp2 !== null) {
        if(temp1.val <= temp2.val) {
            temp.next = temp1
            temp1 = temp1.next
        } else {
            temp.next = temp2 
            temp2 = temp2.next
        }

        temp = temp.next
    }

    if(temp1 || temp2) {
        temp.next = temp1 || temp2
    }

    return head.next
}
````