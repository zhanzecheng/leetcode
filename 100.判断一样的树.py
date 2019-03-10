# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/24 下午4:59
# @Author  : zhanzecheng
# @File    : 100.判断一样的树.py
# @Software: PyCharm
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q != None or p != None and q == None:
            return False
        if p == None and q == None:
            return True
        # 简洁明了
        if p.val == q.val:
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        return False