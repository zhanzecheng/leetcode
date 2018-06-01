# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 下午2:42
# @Author  : zhanzecheng
# @File    : 129.所有根的节点和.py
# @Software: PyCharm
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        if not root:
            return 0
        self.preOrder(root, '')
        return self.result

    def preOrder(self, root, word):
        if not root:
            return
        if root and root.left is None and root.right is None:
            word += str(root.val)
            self.result += int(word)
            return

        word += str(root.val)
        self.preOrder(root.left, word)
        self.preOrder(root.right, word)