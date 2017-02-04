#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai08.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh in ra cac so tu 0 - 6, khong in so 3 va so 6
# Vi du: 0 1 2 4 5
n = 6
for i in range(n+1):
    if i == 3 or i == 6:
        continue
    print i