# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/30 下午11:20
# @Author  : zhanzecheng
# @File    : 108.在有序数组中构建二叉查找树.py
# @Software: PyCharm
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 这种建树题一定要用return的方式来进行建树！！！！！！
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = 0
        if len(nums) == 0:
            return
        r = len(nums) - 1
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildTree(root.left, l, mid - 1, nums)
        root.right = self.buildTree(root.right, mid + 1, r, nums)

        return root

    def buildTree(self, root, left, right, nums):
        if left <= right:
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = self.buildTree(root.left, left, mid - 1, nums)
            root.right = self.buildTree(root.right, mid + 1, right, nums)
        return root



