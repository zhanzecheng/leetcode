# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 下午8:05
# @Author  : zhanzecheng
# @File    : 113.所有路径和.py
# @Software: PyCharm
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        path = []
        self.dfs(root, sum, path)
        return self.result

    def dfs(self, root, sum, path):

        if root:
            if sum == root.val and root.left is None and root.right is None:
                path.append(root.val)
                self.result.append(path)
                return

            # TODO: 这里需要对应的两次copy
            p = path.copy()
            p.append(root.val)
            self.dfs(root.left, sum - root.val, p)
            # TODO: 这里需要对应的两次copy
            p = path.copy()
            p.append(root.val)
            self.dfs(root.right, sum - root.val, p)
        return