# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 上午10:10
# @Author  : zhanzecheng
# @File    : 103.Z字型的二叉树遍历.py
# @Software: PyCharm
"""
class Solution:
    def zigzagLevelOrder(self, root):
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
        count = 0
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
        count = 0
        for key, values in res.items():
            if count % 2 == 0:
                result.append(values)
            else:
                result.append(values[::-1])
            count += 1
        return result