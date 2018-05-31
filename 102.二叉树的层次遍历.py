# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 上午10:01
# @Author  : zhanzecheng
# @File    : 102.二叉树的层次遍历.py
# @Software: PyCharm
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        tmp = []
        root.lev = 0
        tmp.append(root)
        res = {}
        while len(tmp) > 0:
            t = tmp.pop()
            if t.lev not in res:
                res[t.lev] = [t.val]
            else:
                res[t.lev].append(t.val)
            if t.right:
                t.right.lev = t.lev + 1
                tmp.append(t.right)
            if t.left:
                t.left.lev = t.lev + 1
                tmp.append(t.left)
        result = []
        for key, values in res.items():
            result.append(values)
        return result
