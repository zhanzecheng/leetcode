# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 上午10:55
# @Author  : zhanzecheng
# @File    : 106.中序后序建立二叉树.py
# @Software: PyCharm
"""

class Solution:
    def buildTree(self, inorder, preorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [] or inorder == []:
            return None

        self.preorder = preorder
        root = TreeNode(self.preorder[-1])
        self.preorder = self.preorder[:-1]
        root.left = self.build(inorder[:inorder.index(root.val)])
        root.right = self.build(inorder[inorder.index(root.val) + 1:])
        return root

    def build(self, inorder):
        if self.preorder == [] or inorder == []:
            return None

        root = TreeNode(self.preorder[-1])
        self.preorder = self.preorder[:-1]

        root.left = self.build(inorder[:inorder.index(root.val)])
        root.right = self.build(inorder[inorder.index(root.val) + 1:])
        return root