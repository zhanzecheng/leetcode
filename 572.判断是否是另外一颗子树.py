# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 下午1:33
# @Author  : zhanzecheng
# @File    : 572.判断是否是另外一颗子树.py
# @Software: PyCharm
"""

# 利用递归的方式
# 递归的比较每一个节点

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def check(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return check(a.left, b.left) and check(a.right, b.right)

        if not s:
            return False
        flag = check(s, t)
        if flag:
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)