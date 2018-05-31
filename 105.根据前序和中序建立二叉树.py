# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 上午10:12
# @Author  : zhanzecheng
# @File    : 105.根据前序和中序建立二叉树.py
# @Software: PyCharm
"""


# 注意需要区分一次 left和right 的顺序
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
        root.right = self.build(inorder[inorder.index(root.val) + 1:])

        root.left = self.build(inorder[:inorder.index(root.val)])
        return root

    def build(self, inorder):
        if self.preorder == [] or inorder == []:
            return None

        root = TreeNode(self.preorder[-1])
        self.preorder = self.preorder[:-1]
        root.right = self.build(inorder[inorder.index(root.val) + 1:])


        root.left = self.build(inorder[:inorder.index(root.val)])
        return root