#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai11.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh tao ra mang 2 chieu gom co m dong va n cot: voi a_{ij} = i*j
# Vi du: 3 dong 4 cot: [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

m = 3   # So dong
n = 4   # So cot

arr1 = []
for i in range(m):
    arr2 = []   # Reset la mang
    for j in range(n):
        arr2.append(i*j)    # Hang i x cot j
    arr1.append(arr2)

print arr1
