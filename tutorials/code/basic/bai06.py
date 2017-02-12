#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai06.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-basic-exercises.php
# Yeu cau:
# Viet chuong trinh cho phep nhap vao day so va cach nhau boi dau phay.
# Vi du: 2, 3, 5, 7, 11
# In ra: ['2', '3', '5', '7', '11'] va ('2', '3', '5', '7', '11')

dayso = raw_input("Nhap vao day so: ")

lst = dayso.split(',')
tup = tuple(lst)

print lst
print tup