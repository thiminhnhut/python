#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai02.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh tinh tong tat ca cac phan tu cua list

def sumlist(lst):
    """Function: Tinh tong tat ca cac phan tu trong list"""
    s = 0
    for i in lst:
        s = s + i
    return s

a = [8, 2, 3, 0, 7]

# Su dung ham tu dinh nghia
sum_a = sumlist(a)
print "Tong cac phan tu cua {} la: {}".format(a, sum_a)

# Dung ham sum
sum_a = sum(a)
print "Tong cac phan tu cua {} la: {}".format(a, sum_a)