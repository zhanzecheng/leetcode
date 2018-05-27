# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/27 下午5:21
# @Author  : zhanzecheng
# @File    : 56.合并区间.py
# @Software: PyCharm
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        from functools import cmp_to_key
        sort_list = sorted(intervals, key=cmp_to_key(self.cap))
        length = len(sort_list)
        i = 0
        end = sort_list[-1]
        while True:
            # 定义结束标志
            if end == sort_list[i]:
                break
            if sort_list[i].end >= sort_list[i+1].start :
                if end == sort_list[i+1]:
                    if sort_list[i].end < sort_list[i+1].end:
                        sort_list[i].end = sort_list[i+1].end
                    del sort_list[i+1]
                    break
                if sort_list[i].end < sort_list[i+1].end:
                    sort_list[i].end = sort_list[i+1].end
                del sort_list[i+1]

            else:
                i += 1
        return sort_list
    def cap(self, x, y):
        # 如果x要排在y的前面，return -1
        if x.start < y.start:
            return -1
        elif x.start > y.start:
            return 1
        else:
            if x.end < y.end:
                return -1
            else:
                return 1

if __name__ == '__main__':
    data = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
    solution = Solution()
    print(solution.merge(data))