# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/15 上午11:41
# @Author  : zhanzecheng
# @File    : 792.在words中查找单词.py
# @Software: PyCharm
"""

# 这一道题还是很复杂的
# 利用了 hash 和 折半查找的方法
# 使用了一个cur指针来指引目前的单词位置
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        # 这一步先建立一个序号排序
        voca = {}
        for index in range(len(S)):
            if S[index] not in voca:
                voca[S[index]] = [index]
            else:
                voca[S[index]].append(index)

        def is_match(word):
            cur = -1
            for c in word:
                if c not in voca:
                    return False

                values = voca[c]
                # 这里用查找来定位第一个大于cur的数
                find_flag = False
                low = 0
                high = len(values) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if values[mid] > cur:
                        find_flag = True
                        high = mid - 1
                    elif values[mid] < cur:
                        low = mid + 1
                    else:
                        find_flag = True
                        low = mid + 1
                        break
                if low == len(values):
                    return False
                # print(low, values, cur)

                cur = values[low]
                if find_flag == False:
                    return False
            return True

        count = 0
        for word in words:
            if is_match(word):
                count += 1
        return count