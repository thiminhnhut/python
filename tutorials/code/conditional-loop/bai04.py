#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai04.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh in ra hinh duoi:
# *          (n=1)
# * *        (n=2)
# * * *      (n=3)
# * * * *    (n=4)
# * * * * *
# * * * *
# * * *
# * *
# *
n = 4
for i in range(1, n+2):
    for j in range(i+1):
        s = "* "*j
    print s

for i in range(n, 0, -1):
    for j in range(i+1):
        s = "* "*j
    print s
