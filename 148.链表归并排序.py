# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 下午4:05
# @Author  : zhanzecheng
# @File    : 148.链表归并排序.py
# @Software: PyCharm
"""

# TODO: check 1

# 注意这里 在找到中点之后， 是先把其断开，然后再连接
# 归并的思想不错


# 快排的思想也很伟大

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        low = self.findMiddle(head)
        p = low.next
        # 注意这里是先断开，再连接
        low.next = None
        left = self.sortList(head)
        right = self.sortList(p)

        return self.merge(left, right)

    def merge(self, left, right):
        head = ListNode(-1)
        p = head
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        while left:
            p.next = left
            left = left.next
            p = p.next
        while right:
            p.next = right
            right = right.next
            p = p.next
        return head.next

    def findMiddle(self, head):
        low = head
        faster = head
        while faster and faster.next and faster.next.next:
            low = low.next
            faster = faster.next.next
        return low