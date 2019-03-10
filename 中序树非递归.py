# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 上午9:58
# @Author  : zhanzecheng
# @File    : 中序树非递归.py
# @Software: PyCharm
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        re = []
        while root and len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left

            root = stack[-1]
            stack.pop()
            re.append(root.val)
            root = root.right
        return re