# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 下午3:10
# @Author  : zhanzecheng
# @File    : 669.范围删除查找二叉树.py
# @Software: PyCharm
"""

# 这里还有一种更加精巧的解法，用递归来做
class Solution:
    def trimBST(self, root, L, R):
        if not root:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)

        if root.val > R:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        data = []
        self.inOrder(root, data)
        for i in data:
            if i < L or i > R:
                root = self.deleteNode(root, i)
        return root

    def inOrder(self, root, data):
        if not root:
            return

        self.inOrder(root.left, data)
        data.append(root.val)
        self.inOrder(root.right, data)

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
                return cur
                # 左右子树都不为空
                # 找到直接前驱， 替代 并删除前驱

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root