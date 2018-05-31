# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 上午9:19
# @Author  : zhanzecheng
# @File    : 110.平衡二叉树.py
# @Software: PyCharm
"""

# 现求深度 再前序遍历
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.pre_order(root) is not None:
            return False
        return True

    def pre_order(self, root):
        if root:
            l = self.searchDepth(root.left, 1)
            r = self.searchDepth(root.right, 1)
            if abs(l - r) > 1:
                return False

            if self.pre_order(root.left) is not None:
                return False
            if self.pre_order(root.right) is not None:
                return False

    def searchDepth(self, root, num):
        if root:
            num = max(self.searchDepth(root.left, num + 1), self.searchDepth(root.right, num + 1))
            return num
        return num