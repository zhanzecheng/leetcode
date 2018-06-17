# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 上午11:24
# @Author  : zhanzecheng
# @File    : 337.超级抢劫.py
# @Software: PyCharm
"""

# 总结两点的牛逼之处：
# 1） 对树形结构使用DP的方法
# 2） 利用hash来优化时间复杂



# 还是被这个神奇的递归给吓到了，一切都恰到好处
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        val = 0
        if root.left:
            val += self.rob(root.left.left)
            val += self.rob(root.left.right)

        if root.right:
            val += self.rob(root.right.left)
            val += self.rob(root.right.right)

        return max(val + root.val, self.rob(root.left) + self.rob(root.right))