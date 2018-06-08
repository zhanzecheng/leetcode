# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 上午9:36
# @Author  : zhanzecheng
# @File    : 118.二叉树的层次右连接II.py
# @Software: PyCharm
"""

# 做到我吐的一题

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        node = root
        dummy = TreeLinkNode(0)
        tail = dummy
        while node:
            tail.next = None
            if node.left:
                tail.next = node.left
                tail = tail.next

            if node.right:
                tail.next = node.right
                tail = tail.next
            node = node.next
            if not node:
                node = dummy.next
                tail = dummy