# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 下午8:39
# @Author  : zhanzecheng
# @File    : 114.压平树.py
# @Software: PyCharm
"""
# 其实这个解法充满了trick

# TODO: check 1

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.help(root)
    def help(self, root):
        if root is None:
            return
        if self.pre != None:
            self.pre.left = None
            self.pre.right = root
        self.pre = root
        tmp = root.right
        self.help(root.left)
        root.left = None
        self.help(tmp)