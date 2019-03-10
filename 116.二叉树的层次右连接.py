# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 上午9:27
# @Author  : zhanzecheng
# @File    : 116.二叉树的层次右连接.py
# @Software: PyCharm
"""

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        pre = root
        while pre and pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left