# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/29 下午8:05
# @Author  : zhanzecheng
# @File    : 98.判断是否是有效查找二叉树.py
# @Software: PyCharm
"""

# TODO: 值得注意的地方是等号成立的情况

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.data = []
        self._inorder(root)
        if len(self.data) <= 1:
            return True
        pre = self.data[0]
        for i in self.data[1:]:
            if pre >= i:
                return False
            pre = i
        return True

    def _inorder(self, root):
        if root != None:
            self._inorder(root.left)
            self.data.append(root.val)
            self._inorder(root.right)