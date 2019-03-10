# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/29 下午2:49
# @Author  : zhanzecheng
# @File    : 95.产生所有的不同的排序二叉树.py
# @Software: PyCharm
"""

# TODO: 这个其实也不太会
# TODO: 这一题是真的难！！
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTrees(1, n)


    def genTrees(self, start, end):

        data = []
        # 不懂为啥要这样
        if start > end:
            data.append(None)
            return data

        if start == end:
            data.append(TreeNode(start))
            return data

        for i in range(start, end + 1):
            left = self.genTrees(start, i - 1)
            right = self.genTrees(i + 1, end)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    data.append(root)
        return data
if __name__ == '__main__':
    solution = Solution()
    print(solution.generateTrees(3))