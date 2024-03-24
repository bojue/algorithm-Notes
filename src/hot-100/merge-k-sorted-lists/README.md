
# 23. 合并 K 个升序链表

## 相关标签

- 链表
- 分治
- 堆（优先队列）
- 归并排序

## 问题描述 

23. 合并 K 个升序链表 - 给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6


示例 2：

输入：lists = []
输出：[]


示例 3：

输入：lists = [[]]
输出：[]


 

提示：

 * k == lists.length
 * 0 <= k <= 10^4
 * 0 <= lists[i].length <= 500
 * -10^4 <= lists[i][j] <= 10^4
 * lists[i] 按 升序 排列
 * lists[i].length 的总和不超过 10^4

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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    const len = lists.length 
    if(!len) {
        return null
    }

    if(len === 1) {
        return lists[0]
    }
    let result = null
    for(let i=0;i<len;i++) {
        result = merge(result, lists[i])
    }

    return result
};

function merge(l1, l2) {
    const newHead =  new ListNode();
    let curr = newHead
    while(l1 && l2) {
        if(l1.val < l2.val) {
            curr.next = l1 
            l1 = l1.next
        } else {
            curr.next = l2
            l2 = l2.next
        }

        curr = curr.next
    }

    if(l1 || l2) {
        curr.next = l1 || l2
    }

    return newHead.next
}
````