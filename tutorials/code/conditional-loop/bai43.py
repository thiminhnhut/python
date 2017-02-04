#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai43.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh in ra bang cuu chuong tu 1-10 cho mot so

n = int(raw_input("Nhap vao mot so: "))

for i in range(10):
    print "{} x {} = {}".format(n, i+1, n*(i+1))