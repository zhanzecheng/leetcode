# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/24 下午2:11
# @Author  : zhanzecheng
# @File    : 652.寻找二叉树多余的子树.py
# @Software: PyCharm
"""

# 利用后序遍历的字符串看看字串是否有重复，并且用map来降低时间复杂度


# 核心是用字符串来表示一颗数

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.dic = {}

        if not root:
            return []

        self.posOrder(root)
        result = []
        for key, values in self.dic.items():
            if len(values) > 1:
                result.append(values[0])
        return result

    def posOrder(self, root):
        if not root:
            return "NULL"

        a = self.posOrder(root.left)
        b = self.posOrder(root.right)
        re = a + b + str(root.val)

        if re not in self.dic:
            self.dic[re] = [root]
        else:
            self.dic[re].append(root)
        return re