# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/23 下午8:26
# @Author  : zhanzecheng
# @File    : 88.Merge_Sorted_Array.py
# @Software: PyCharm
"""

"""
这一题有更好的解法，从大往小解法
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1.copy()
        i = 0
        j = 0
        count = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                tmp[count] = nums1[i]
                i += 1
            else:
                tmp[count] = nums2[j]
                j += 1
            count += 1
        while i < m:
            tmp[count] = nums1[i]
            i += 1
            count += 1
        while j < n:
            tmp[count] = nums2[j]
            j += 1
            count += 1
        # 单纯的指引并不会改变引用，一定要一个一个赋值
        nums1[:] = tmp[:]

def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]


if __name__ == '__main__':
    solution = Solution()
    data1 = [1,2,3,0,0,0]
    m = 3
    data2 = [2, 5, 6]
    n = 3
    print(solution.merge(data1, m, data2, n))