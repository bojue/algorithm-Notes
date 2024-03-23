# Algorithm


## 构建脚本

`Bojue` 前端算法笔记

### 1. 根据题目自动创建题目（手动更新）

场景：完成题目，根据题目名称创建对应的题目笔记


```shell

# mac上执行
# window要自测

python3 script-create-readme.py
```


### 2. 更新最新的数据（自动更新）

场景：习题题解更新，可以执行全部更新算法笔记，获取全部的最新笔记内容，题解只获取最新通过的题目


1. 配置config.json，统计leetcode接口需要

```shell

{
  "csrftoken": "",
  "Cookie": ""
}
```


2. 执行统计脚本


```shell

# mac上执行
# window要自测

python3 script-update-latest.py
```



### 3. 更新统计README

场景：更新完毕题目笔记，更新最新的统计数据

```shell

# mac上执行
# window要自测

python3 script-statistics-readme.py
```

## 题目统计




统计数据 => 总数量：<font color="#336df4" >100</font>  , 已经完成 <font color="#1dddae" >85</font> , 百分比例 <font color="#1dddae" >85%</font>

## 题目列表
[54. 螺旋矩阵](src/hot-100/spiral-matrix/README.md)

[200. 岛屿数量](src/hot-100/number-of-islands/README.md)

[70. 爬楼梯](src/hot-100/climbing-staris/README.md)

[41. 缺失的第一个正数](src/hot-100/first-missing-positive/README.md)

[128. 最长连续序列](src/hot-100/longest-consecutive-sequence/README.md)

[34. 在排序数组中查找元素的第一个和最后一个位置](src/hot-100/find-first-and-last-position-of-element-in-sorted-array/README.md)

[543. 二叉树的直径](src/hot-100/diameter-of-binary-tree/README.md)

[56. 合并区间](src/hot-100/merge-intervals/README.md)

[146. LRU 缓存](src/hot-100/lru-cache/README.md)

[20. 有效的括号](src/hot-100/valid-parentheses/README.md)

[1. 两数之和](src/hot-100/tow-sun/README.md)

[102. 二叉树的层序遍历](src/hot-100/binary-tree-level-order-traversal/README.md)

[76. 最小覆盖子串](src/hot-100/minimum-window-substring/README.md)

[438. 找到字符串中所有字母异位词](src/hot-100/find-all-anagrams-in-a-string/README.md)

[207. 课程表](src/hot-100/course-schedule/README.md)

[139. 单词拆分](src/hot-100/word-break/README.md)

[98. 验证二叉搜索树](src/hot-100/validate-binary-search-tree/README.md)

[131. 分割回文串](src/hot-100/palindrome-partitioning/README.md)

[20. 不同路径](src/hot-100/unique-paths/README.md)

[114. 二叉树展开为链表](src/hot-100/flatten-binary-tree-to-linked-list/README.md)

[136. 只出现一次的数字](src/hot-100/signal-number/README.md)

[121. 买卖股票的最佳时机](src/hot-100/best-time-to-buy-and-sell-stock/README.md)

[94. 二叉树的中序遍历](src/hot-100/binary-tree-inorder-traversal/README.md)

[105. 从前序与中序遍历序列构造二叉树](src/hot-100/construct-binary-tree-from-preorder-and-inorder-traversal/README.md)

[23. 合并 K 个升序链表](src/hot-100/merge-k-sorted-lists/README.md)

[108. 将有序数组转换为二叉搜索树](src/hot-100/convert-sorted-array-to-binary-search-tree/README.md)

[155. 最小栈](src/hot-100/min-stack/README.md)

[124. 二叉树中的最大路径和](src/hot-100/binary-tree-maximum-path-sum/README.md)

[240. 搜索二维矩阵 II](src/hot-100/search-a-2d-matrix-ii/README.md)

[1. 两数之和](src/hot-100/two-sum/README.md)

[206. 反转链表](src/hot-100/reverse-linked-list/README.md)

[198. 打家劫舍](src/hot-100/house-robber/README.md)

[24. 两两交换链表中的节点](src/hot-100/swap-nodes-in-pairs/README.md)

[35. 搜索插入位置](src/hot-100/search-insert-position/README.md)

[55. 跳跃游戏](src/hot-100/jump-game/README.md)

[64. 最小路径和](src/hot-100/minimum-path-sum/README.md)

[208. 实现 Trie (前缀树)](src/hot-100/implement-trie-prefix-tree/README.md)

[33. 搜索旋转排序数组](src/hot-100/search-in-rotated-sorted-array/README.md)

[17. 电话号码的字母组合](src/hot-100/letter-combinations-of-a-phone-number/README.md)

[39. 组合总和](src/hot-100/combination-sum/README.md)

[48. 旋转图像](src/hot-100/rotate-image/README.md)

[142. 环形链表 II](src/hot-100/linked-list-cycle-ii/README.md)

[3. 无重复字符的最长子串](src/hot-100/longest-substring-without-repeating-characters/README.md)

[15. 三数之和](src/hot-100/3sum/README.md)

[283. 移动零](src/hot-100/move-zeroes/README.md)

[160. 相交链表](src/hot-100/intersection-of-two-linked-lists/README.md)

[25. K 个一组翻转链表](src/hot-100/reverse-nodes-in-k-group/README.md)

[239. 滑动窗口最大值](src/hot-100/sliding-window-maximum/README.md)

[4. 寻找两个正序数组的中位数](src/hot-100/median-of-two-sorted-arrays/README.md)

[153. 寻找旋转排序数组中的最小值](src/hot-100/find-minimum-in-rotated-sorted-array/README.md)

[238. 除自身以外数组的乘积](src/hot-100/product-of-array-except-self/README.md)

[84. 柱状图中最大的矩形](src/hot-100/largest-rectangle-in-histogram/README.md)

[394. 字符串解码](src/hot-100/decode-string/README.md)

[53. 最大子数组和](src/hot-100/maximum-subarray/README.md)

[437. 路径总和 III](src/hot-100/path-sum-iii/README.md)

[994. 腐烂的橘子](src/hot-100/rotting-oranges/README.md)

[230. 二叉搜索树中第K小的元素](src/hot-100/kth-smallest-element-in-a-bst/README.md)

[104. 二叉树的最大深度](src/hot-100/maximum-depth-of-binary-tree/README.md)

[49. 字母异位词分组](src/hot-100/group-anagrams/README.md)

[189. 轮转数组](src/hot-100/rotate-array/README.md)

[169. 多数元素](src/hot-100/majority-elemen/README.md)

[739. 每日温度](src/hot-100/daily-temperatures/README.md)

[42. 接雨水](src/hot-100/trapping-rain-water/README.md)

[560. 和为 K 的子数组](src/hot-100/subarray-sum-equals-k/README.md)

[101. 对称二叉树](src/hot-100/symmetric-tree/README.md)

[226. 翻转二叉树](src/hot-100/invert-binary-tree/README.md)

[22. 括号生成](src/hot-100/generate-parentheses/README.md)

[148. 排序链表](src/hot-100/sort-list/README.md)

[199. 二叉树的右视图](src/hot-100/binary-tree-right-side-view/README.md)

[73. 矩阵置零](src/hot-100/set-matrix-zeroes/README.md)

[19. 删除链表的倒数第 N 个结点](src/hot-100/remove-nth-node-from-end-of-list/README.md)

[141. 环形链表](src/hot-100/linked-list-cycle/README.md)

[21. 合并两个有序链表](src/hot-100/merge-two-sorted-lists/README.md)

[78. 子集](src/hot-100/subsets/README.md)

[138. 随机链表的复制](src/hot-100/copy-list-with-random-pointer/README.md)

[234. 回文链表](src/hot-100/palindrome-linked-list/README.md)

[46. 全排列](src/hot-100/permutations/README.md)

[74. 搜索二维矩阵](src/hot-100/search-a-2d-matrix/README.md)

[2. 两数相加](src/hot-100/add-two-numbers/README.md)

[11. 盛最多水的容器](src/hot-100/container-with-most-water/README.md)

[51. N 皇后](src/hot-100/n-queens/README.md)

[236. 二叉树的最近公共祖先](src/hot-100/lowest-common-ancestor-of-a-binary-tree/README.md)

[79. 单词搜索](src/hot-100/word-search/README.md)

[322. 零钱兑换](src/hot-100/coin-change/README.md)

