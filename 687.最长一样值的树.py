# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 下午3:02
# @Author  : zhanzecheng
# @File    : 687.最长一样值的树.py
# @Software: PyCharm
"""

# 疯狂的递归
# 这一道题还是挺难的

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        val = self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
        val = max(val, self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))
        return val

    def dfs(self, root, val):
        if not root:
            return 0
        count = 0
        if root.val == val:
            count += 1
            count += max(self.dfs(root.left, val), self.dfs(root.right, val))

        return count