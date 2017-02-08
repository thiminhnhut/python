#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai05.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh tinh giai thua cua mot so nguyen khong am theo phuong phap de quy.

def fact(n):
    """Function: Tinh giai thua cua mot so nguyen khong am theo phuong phap de quy"""
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def fact2(n):
    """Function: Tinh giai thua cua mot so nguyen khong am theo dinh nghia"""
    gt = 1
    for i in range(n):
        gt = gt*(i+1)
    return gt

a = 5
# Su dung ham tu dinh nghia
giaithua = fact(a)
print "Giai thua cua {} la: {}".format(a, giaithua)

giaithua = fact2(a)
print "Giai thua cua {} la: {}".format(a, giaithua)

# Su dung ham math.factorial
import math
giaithua = math.factorial(a)
print "Giai thua cua {} la: {}".format(a, giaithua)