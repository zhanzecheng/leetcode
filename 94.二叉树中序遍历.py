# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/29 下午2:12
# @Author  : zhanzecheng
# @File    : 94.二叉树中序遍历.py
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
        self.result = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self._inorder(root)
        return self.result
    def _inorder(self, root):
        if root != None:
            self._inorder(root.left)
            self.result.append(root.val)
            self._inorder(root.right)