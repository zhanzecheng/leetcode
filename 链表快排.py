# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 下午3:19
# @Author  : zhanzecheng
# @File    : 链表快排.py
# @Software: PyCharm
"""

# TODO: check 1
# 链表快排
# 这里需要注意是return head
class Solution:
    def partition(self, head, tail):
        if not head:
            return head
        if head == tail:
            return head
        pre = ListNode(-1)
        pre.next = head
        low = head
        cur = head
        while low.next != tail:
            # 注意这里是用if来判断
            if low.next.val < cur.val:
                tmp = low.next
                low.next = low.next.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                low = low.next
        pre.next = self.partition(pre.next, cur)
        while cur and cur.next and cur.val == cur.next.val:
            cur = cur.next
        cur.next = self.partition(cur.next, tail)

        return pre.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head = self.partition(head, None)
        return head