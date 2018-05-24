# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/24 下午7:24
# @Author  : zhanzecheng
# @File    : 112.树-节点和.py
# @Software: PyCharm
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            if root.left == None and root.right == None:
                if root.val == sum:
                    return True
                else:
                    return False
            if self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val):
                return True
            return False
        else:
            return False
