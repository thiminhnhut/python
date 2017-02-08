#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai01.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh tim so lon nhat trong 3 so

def max3(a, b, c):
    """Function: Tim so lon nhat trong 3 so"""
    nmax = a
    if b > nmax:
        nmax = b
    if c > nmax:
        nmax = c
    return nmax

a = 1
b = 2
c = 3

# Su dung ham tu dinh nghia
solonnhat = max3(a, b, c)
print "So lon nhat trong 3 so {} {} {} la {}".format(a, b, c, solonnhat)

# Su dung ham max
solonnhat = max(a, b, c)
print "So lon nhat trong 3 so {} {} {} la {}".format(a, b, c, solonnhat)