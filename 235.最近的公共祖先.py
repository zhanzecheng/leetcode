# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/10 上午10:45
# @Author  : zhanzecheng
# @File    : 235.最近的公共祖先.py
# @Software: PyCharm
"""

# 对于BST这么做是比较靠谱的
"""

def lowestCommonAncestor(self, root, p, q):
    if p.val < root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)
    if p.val > root.val < q.val:
        return self.lowestCommonAncestor(root.right, p, q)
    return root
    
"""

# 对于普通二叉树这么做比较靠谱
"""
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else (left or right)
        
"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.re1 = []
        self.re2 = []
        self.preOrder1(root, p, [])
        self.preOrder2(root, q, [])
        length = min(len(self.re1), len(self.re2))
        re = None
        for i in range(length):
            if self.re1[i] == self.re2[i]:
                re = self.re1[i]
            else:
                break
        return re

    def preOrder1(self, root, target, tmp):
        if not root:
            tmp.append(None)
            return

        if root == target:
            tmp.append(root)
            self.re1 = tmp.copy()
            return
        tmp.append(root)

        self.preOrder1(root.left, target, tmp)
        tmp.pop()
        self.preOrder1(root.right, target, tmp)
        tmp.pop()

    def preOrder2(self, root, target, tmp):
        if not root:
            tmp.append(None)
            return

        if root == target:
            tmp.append(root)
            self.re2 = tmp.copy()
            return
        tmp.append(root)

        self.preOrder2(root.left, target, tmp)
        tmp.pop()
        self.preOrder2(root.right, target, tmp)
        tmp.pop()