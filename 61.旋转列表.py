# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/27 下午8:37
# @Author  : zhanzecheng
# @File    : 61.旋转列表.py
# @Software: PyCharm
"""


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # TODO: p, p->next
        p = head
        if p == None:
            return None
        if p.next == None:
            if k % 2 == 0:
                return head
            else:
                return head
        length = 0
        while p != None:
            p = p.next
            length += 1
        k = k % length
        while k > 0:
            p = head
            while p.next.next != None:
                p = p.next
            tmp = p.next
            p.next = None
            tmp.next = head
            head = tmp
            k -= 1
        return head