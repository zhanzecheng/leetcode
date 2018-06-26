# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/25 上午10:20
# @Author  : zhanzecheng
# @File    : 735.小行星碰撞.py
# @Software: PyCharm
"""


class Solution:
    def asteroidCollision(self, nums):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        if not nums:
            return None

        # 初步的思考是使用栈的方式来做
        stack = []
        re = []
        flag = False

        for i in nums:
            if i < 0 and flag == False:
                re.append(i)
            elif i < 0 and flag == True:
                if len(stack) == 0:
                    re.append(i)
                else:
                    # TODO: 这里应该有条件判断
                    reee = False
                    while len(stack) > 0:
                        tmp = stack.pop()
                        if tmp > -i:
                            stack.append(tmp)
                            break
                        elif tmp == -i:
                            reee = True
                            break
                    if len(stack) == 0 and reee == False:
                        re.append(i)
            elif i > 0:
                flag = True
                stack.append(i)
        return re + stack