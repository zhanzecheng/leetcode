# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 下午3:24
# @Author  : zhanzecheng
# @File    : 654.构建最大二叉树.py
# @Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if len(nums) == 0:
            return None
        max_val = -1
        max_cur = -1
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                max_cur = i

        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_cur])
        root.right = self.constructMaximumBinaryTree(nums[max_cur+1:])
        return root