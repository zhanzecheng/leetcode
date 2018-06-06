# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/5 下午1:51
# @Author  : zhanzecheng
# @File    : 142.检测链表的圈起始位置.py
# @Software: PyCharm
"""


# 这个公式其实不太明白
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        faster = head
        slow = head
        while faster and faster.next:
            slow = slow.next
            faster = faster.next.next
            if slow == faster:
                cur = head
                while cur != slow:
                    cur = cur.next
                    slow = slow.next
                return cur
        return None