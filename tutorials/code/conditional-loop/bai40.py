#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai40.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh tinh trung binh cua 3 so nguyen duoc nhap tu ban phim.
# Vi du: 1 2 4 --> 2; 4 6 5 --> 5

a = float(raw_input("Nhap so thu nhat: "))
b = float(raw_input("Nhap so thu hai: "))
c = float(raw_input("Nhap so thu b: "))

if a < b:
    if a < c:
        if b < c:
            median = b
        else:
            median = c
    else:
        median = a
else:
    if c > a:
        median = a
    else:
        if c > b:
            median = c
        else:
            median = b

print median