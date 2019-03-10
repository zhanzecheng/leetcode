# -*- coding: utf-8 -*-
"""
# @Time    : 2017/9/24 下午4:30
# @Author  : zhanzecheng
# @File    : 4_add_Two_Numbers.py
# @Software: PyCharm
"""

'''
可更改变量与不可更改对象
nfoo = 1
nfoo = 2

lstFoo = [1]
lstFoo[0] = 2

a = [1,2]
b = a
b[0] = 10
print a

'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

