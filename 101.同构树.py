# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/30 下午10:48
# @Author  : zhanzecheng
# @File    : 101.同构树.py
# @Software: PyCharm
"""

# 这个可以先前序再中序

# 还有一种优化算法就是只遍历一次，但是是左，右的顺序，加上判别是不是同一棵树的老套路

# TODO: check 1
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l1 = []
        l2 = []
        r1 = []
        r2 = []
        if root is None:
            return True
        self.pre_ord(root.left, l1)
        self.in_order(root.left, l2)
        self.pre_ord2(root.right, r1)
        self.in_order2(root.right, r2)
        return l1 == r1 and l2 == r2

    def pre_ord(self, root, result):
        if root:
            result.append(root.val)
            self.pre_ord(root.left, result)
            self.pre_ord(root.right, result)

    def pre_ord2(self, root, result):
        if root:
            result.append(root.val)
            self.pre_ord2(root.right, result)
            self.pre_ord2(root.left, result)

    def in_order(self, root, result):
        if root:
            self.in_order(root.left, result)
            result.append(root.val)
            self.in_order(root.right, result)

    def in_order2(self, root, result):
        if root:
            self.in_order2(root.right, result)
            result.append(root.val)
            self.in_order2(root.left, result)