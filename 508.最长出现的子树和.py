# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/17 上午11:01
# @Author  : zhanzecheng
# @File    : 508.最长出现的子树和.py
# @Software: PyCharm
"""

# 这个也就是使用了dfs 和 哈希 来加速

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dic = {}
        self.preOrder(root)
        re = {}
        count = 0
        for _, value in self.dic.items():
            if value not in re:
                re[value] = 1
            else:
                re[value] += 1
            if re[value] > count:
                count = re[value]
        result = []
        for key, value in re.items():
            if value == count:
                result.append(key)
        return result
    def preOrder(self, root):
        if not root:
            return 0

        if root not in self.dic:
            if root.left not in self.dic:
                l = self.preOrder(root.left)
            else:
                l = self.dic[root.left]

            if root.right not in self.dic:
                r = self.preOrder(root.right)
            else:
                r = self.dic[root.right]

            self.dic[root] = root.val + l + r

        return self.dic[root]