# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/23 下午3:07
# @Author  : zhanzecheng
# @File    : 692.前K个词频.py
# @Software: PyCharm
"""

# 这一题好需要 好好整理一下优先队列， 类的比较函数的使用
import heapq
class Skill:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):  # operator <
        if self.priority == other.priority:
            return self.description > other.description
        return self.priority < other.priority
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = {}
        for i in words:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        queue = []
        for key, value in dic.items():
            if len(queue) < k:
                heapq.heappush(queue, Skill(value, key))
            else:
                tmp = heapq.heappop(queue)
                if  Skill(value, key) < tmp:
                    heapq.heappush(queue, tmp)
                else:
                    heapq.heappush(queue, Skill(value, key))
        re = []
        for _ in range(k):
            re.append(heapq.heappop(queue).description)
        return re[::-1]
if __name__ == '__main__':
    soliution = Solution()
    data = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(soliution.topKFrequent(data, k))