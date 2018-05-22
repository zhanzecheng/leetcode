# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/22 下午9:09
# @Author  : zhanzecheng
# @File    : 24.Swap_Nodes_inPairs.py
# @Software: PyCharm
"""


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        tmp = head
        while tmp != None:
            tmp = tmp.next
            length += 1
        if length % 2 != 0:
            length -= 1
        tmp = head
        count = 0
        pre = ListNode(10)
        pre.next = head
        head = pre
        while count < length:
            before = tmp
            after = tmp.next
            tmp = tmp.next.next
            before.next = after.next
            after.next = before
            pre.next = after
            pre = before
            count += 2
        return head.next