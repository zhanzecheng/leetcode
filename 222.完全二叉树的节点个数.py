# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/9 上午11:33
# @Author  : zhanzecheng
# @File    : 222.完全二叉树的节点个数.py
# @Software: PyCharm
"""

# 这一道题递归用的真是好
class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.find_left(root)
        r = self.find_right(root)
        if l == r:
            return (1 << l) - 1
        else:
            return self.countNodes(root.left) + 1 + self.countNodes(root.right)

    def find_right(self, root):
        count = 0
        while root:
            count += 1
            root = root.right
        return count

    def find_left(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count