# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 上午10:12
# @Author  : zhanzecheng
# @File    : 105.根据前序和中序建立二叉树.py
# @Software: PyCharm
"""


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [] or inorder == []:
            return None

        self.preorder = preorder
        root = TreeNode(self.preorder[0])
        self.preorder = self.preorder[1:]
        root.left = self.build(inorder[:inorder.index(root.val)])
        root.right = self.build(inorder[inorder.index(root.val) + 1:])
        return root

    def build(self, inorder):
        if self.preorder == [] or inorder == []:
            return None

        root = TreeNode(self.preorder[0])
        self.preorder = self.preorder[1:]

        root.left = self.build(inorder[:inorder.index(root.val)])
        root.right = self.build(inorder[inorder.index(root.val) + 1:])
        return root