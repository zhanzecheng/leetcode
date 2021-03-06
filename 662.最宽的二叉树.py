# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/14 下午3:02
# @Author  : zhanzecheng
# @File    : 662.最宽的二叉树.py
# @Software: PyCharm
"""
# 难，这题是保存位置信息来做
# 这一题的本质上其实是一个层次遍历

# TODO: check 1
class Solution(object):
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        cur_depth = left= ans = 0
        # 这里使用一个for循环来遍历
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if depth != cur_depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans