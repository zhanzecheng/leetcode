# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/30 下午10:15
# @Author  : zhanzecheng
# @File    : 92.翻转链表.py
# @Software: PyCharm
"""


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        pre = ListNode(-1)
        pre.next = head
        p = head
        head = pre
        left = 0
        right = 0
        while p and p.next:
            left += 1
            right += 1

            if left >= m and right < n:
                tmp = p.next
                p.next = p.next.next
                tmp.next = pre.next
                pre.next = tmp

            else:
                pre = pre.next
                p = p.next

        return head.next