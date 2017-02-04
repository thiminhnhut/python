#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai44.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh in ra hinh duoi:
# 1          (n=1)
# 22         (n=2)
# 333        (n=3)
# 4444       (n=4)
# 55555      (n=5)
# 666666     (n=6)
# 7777777    (n=7)
# 88888888   (n=8)
# 999999999  (n=9)

n = 9
for i in range(1, n+1):
    for j in range(i+1):
        s = str(i)*j
    print s