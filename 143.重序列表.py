# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/5 上午11:13
# @Author  : zhanzecheng
# @File    : 143.重序列表.py
# @Software: PyCharm
"""


# 这里是用一个堆和一个队列来实现堆

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        stack = []
        quene = []
        p = head
        while p != None:
            stack.append(p)
            quene.append(p)
            p = p.next
        p = head
        count = 0
        for a, b in zip(quene, stack[::-1]):
            count += 1

            if p != head:
                p.next = a
            a.next = b
            b.next = None
            p = b
            if count == len(stack) // 2:
                break

        if len(stack) % 2 == 1:
            b.next = quene[(len(quene) + 1) // 2 - 1]
            b.next.next = None