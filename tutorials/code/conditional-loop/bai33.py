#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai33.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh cho biet so ngay cua thang
# Danh sach cac thang:
# ['January', 'February', 'March', 'April', 'May', 'June',
# 'July', 'August', 'September', 'October', 'November', 'December']
# Vi du: Nhap vao February --> 28/29 ngay

thang = raw_input("Nhap vao ten thang: ")

# Thang 30 ngay
thang30 = ['April','June', 'September', 'November']
thang31 = ['January','March', 'May', 'July', 'August', 'October', 'December']

if thang in thang30:
    print "{} co 30 ngay".format(thang)
elif thang in thang31:
    print "{} co 31 ngay".format(thang)
else:
    print "{} co 28/29 ngay".format(thang)
