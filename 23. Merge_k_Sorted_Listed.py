# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/21 下午5:46
# @Author  : zhanzecheng
# @File    : 23. Merge_k_Sorted_Listed.py
# @Software: PyCharm
"""
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        quene = []
        for node in lists:
            if node: heapq.heappush(quene, [node.val, node])
            # if node: q.put((node.val,node))
        while len(quene) > 0:
            curr.next = heapq.heappop(quene)[1]
            curr=curr.next
            if curr.next: heapq.heappush(quene, [curr.next.val, curr.next])
        return dummy.next