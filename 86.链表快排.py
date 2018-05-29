# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/29 下午8:16
# @Author  : zhanzecheng
# @File    : 86.链表快排.py
# @Software: PyCharm
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        prep = ListNode(x + 1)
        prep.next = head

        p = prep
        pp = prep
        while pp and pp.next:

            if pp.next.val < x:
                if p == pp:
                    pp = pp.next
                    p = p.next
                    continue
                tmp = pp.next
                pp.next = pp.next.next
                tmp.next = p.next
                p.next = tmp
                p = tmp

            else:
                pp = pp.next

        return prep.next

