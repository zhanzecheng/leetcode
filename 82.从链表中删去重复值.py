# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/29 上午9:42
# @Author  : zhanzecheng
# @File    : 82.从链表中删去重复值.py
# @Software: PyCharm
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p = head
        if head == None:
            return head
        # 判断是否只有一个节点
        if p.next == None:
            return head
        # 判断是否只有两个节点
        p = p.next
        while p.val == head.val:
            while p != None:
                if p.val != head.val:
                    head = p
                    break
                p = p.next

            if p == None:
                return None
            p = head
            p = p.next
            if p == None:
                return head
        p = head
        pre = p
        if p == None or p.next == None:
            return p
        p = p.next
        # 现在只有有大于两个节点，并且前两个节点互不相同的情况
        flag = True
        while p.next:
            if p.val == p.next.val:
                flag = False
                pre.next = p.next
                p = p.next
            else:
                if flag == False:
                    pre.next = p.next
                    flag = True
                    p = p.next
                else:
                    pre = p
                    p = p.next
        if flag == False:
            pre.next = p.next
            flag = True
            p = p.next
        return head
