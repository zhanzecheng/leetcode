# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/15 上午10:34
# @Author  : zhanzecheng
# @File    : 450.在排序二叉树中删除节点.py
# @Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这里使用root.left = xxx 这种形式来保存更改的值

# TODO: check 1

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return

        if root.val == key:
            # delete

            # 如果左右子树都为空
            if not root.left and not root.right:
                root = None
                return root
            # 如果只有一个子树为空
            elif not root.left or not root.right:
                root = root.left if root.left else root.right
                return root
            else:
                cur = root.right
                pre = root
                while cur.left:
                    pre = cur
                    cur = cur.left
                if pre == root:
                    pre.right = cur.right
                else:
                    pre.left = cur.right
                cur.right = root.right
                cur.left = root.left
                del root
                return cur
                # 左右子树都不为空
                # 找到直接后驱， 替代 并删除前驱

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root