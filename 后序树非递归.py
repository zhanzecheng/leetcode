# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 上午10:45
# @Author  : zhanzecheng
# @File    : 后序树非递归.py
# @Software: PyCharm
"""


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ans = []
        stack = []
        if root == None:
            return ans

        stack.append(root)

        while len(stack) != 0:
            cur = stack.pop()
            ans = [cur.val] + ans
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return ans