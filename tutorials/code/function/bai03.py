#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai03.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh tinh tich tat ca cac phan tu cua list

def multilist(lst):
    """Function: Tinh tich tat ca cac phan tu trong list"""
    s = 1
    for i in lst:
        s = s * i
    return s

a = [8, 2, 3, -1, 7]
mul_a = multilist(a)
print "Tich cac phan tu cua {} la: {}".format(a, mul_a)