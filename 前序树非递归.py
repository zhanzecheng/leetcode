# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 上午10:41
# @Author  : zhanzecheng
# @File    : 前序树非递归.py
# @Software: PyCharm
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        re = []
        while root or len(stack) != 0:


            while root:
                re.append(root.val)
                stack.append(root)
                root = root.left

            root = stack[-1]
            stack.pop()
            root = root.right
        return re