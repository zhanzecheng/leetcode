# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 下午7:21
# @Author  : zhanzecheng
# @File    : 109.依据有序链表转成二叉树.py
# @Software: PyCharm
"""

# 具体思路: 每一次找中间， 然后递归的建立左右子树

# 做了半天。。。。。。

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        slow = head
        fast = head
        pre = TreeNode(-1)
        pre.next = head
        while fast and fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        if not head.next:
            return root
        pre.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root