# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/24 下午7:22
# @Author  : zhanzecheng
# @File    : 111.Minimum_Depth_of_binary_tree.py
# @Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.min = 10000000

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self._search(root, 1)
        return self.min

    def _search(self, root, count):
        if root:
            if root.left == None and root.right == None:
                self.min = min(count, self.min)
            self._search(root.left, count + 1)
            self._search(root.right, count + 1)








