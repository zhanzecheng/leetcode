# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/21 下午5:46
# @Author  : zhanzecheng
# @File    : 23. Merge_k_Sorted_Listed.py
# @Software: PyCharm
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """

        :param lists: List[ListNode]
        :return:ListNode
        """
        length = len(lists)

        data = []
        for i in range(length):
            tmp = lists[i]
            while tmp != None:
                data.append(tmp.val)
                tmp = tmp.next
        data.sort()
        head = ListNode(0)
        p = head
        for d in data:
            tmp = ListNode(d)
            p.next = tmp
            p = tmp
        return head.next