# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/30 下午11:18
# @Author  : zhanzecheng
# @File    : 107.从底部层次遍历.py
# @Software: PyCharm
"""


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        node = []
        result = []
        if not root:
            return []
        root.level = 0
        node.append(root)
        l = {}
        while len(node) > 0:
            tmp = node.pop()
            if tmp.level not in l:
                l[tmp.level] = [tmp.val]
            else:
                l[tmp.level].append(tmp.val)

            if tmp.right:
                tmp.right.level = tmp.level + 1
                node.append(tmp.right)
            if tmp.left:
                tmp.left.level = tmp.level + 1
                node.append(tmp.left)
        re = []
        for a, b in l.items():
            re.insert(0, b)
        return re