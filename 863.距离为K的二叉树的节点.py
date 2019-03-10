# -*- coding: utf-8 -*-
"""
# @Time    : 2018/7/3 下午9:12
# @Author  : zhanzecheng
# @File    : 863.距离为K的二叉树的节点.py
# @Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root:
            return []
        dic = {}

        def loc(node, pre):
            if not node:
                return
            dic[node] = pre
            loc(node.left, node)
            loc(node.right, node)

        loc(root, None)

        # 这里定义一下BFS
        visit = []
        res = []

        def bfs(node, k):
            if not node:
                return

            if node in visit:
                return
            if k == 0:
                res.append(node.val)
                return
            visit.append(node)
            bfs(node.left, k - 1)
            bfs(node.right, k - 1)
            bfs(dic[node], k - 1)

        bfs(target, K)
        return res