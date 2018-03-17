# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/16 下午3:57
# @Author  : zhanzecheng
# @File    : 4_median_of_two_sorted_array.py
# @Software: PyCharm
"""
'''
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

'''

'''
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''



class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        ood_flag = True
        if (length1 + length2) % 2 == 0:
            ood_flag = False
        total_count = int((length1 + length2) / 2)
        index1 = 0
        index2 = 0
        media = 0
        after = 0
        for i in range(total_count):
            if index1 == length1:
                media = nums2[index2]
                index2 += 1
                continue
            elif index2 == length2:
                media = nums1[index1]
                index1 += 1
                continue
            else:
                if nums1[index1] < nums2[index2]:
                    media = nums1[index1]
                    index1 += 1
                else:
                    media = nums2[index2]
                    index2 += 1

        if index1 == length1:
            final = nums2[index2]
        elif index2 == length2:
            final = nums1[index1]
        else:
            final = min(nums1[index1], nums2[index2])
        if ood_flag:
            return final
        else:
            return (media + final) / 2