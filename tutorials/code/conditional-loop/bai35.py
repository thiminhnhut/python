#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai35.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh kiem tra chuoi nhap vao co phai la so nguyen hay khong?
# Vi du:
# Nhap vao: Python --> Khong phai so nguyen
# Nhap vao: +124 --> La so nguyen

chuoi = raw_input("Input a string: ")
chuoi = chuoi.strip() # Loai bo ky tu trong o hai dau
kt = True
if chuoi[0] in "+-":
    chuoitam = chuoi[1:]
else:
    chuoitam = chuoi

for i in chuoitam:
    if i not in "0123456789":
        kt = False
if kt:
    print "{} la so nguyen".format(chuoi)
else:
    print "{} khong la so nguyen".format(chuoi)