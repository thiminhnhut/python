#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai02.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh chuyen doi nhiet do: C --> F va F --> C. Lam tron ket qua chuyen doi 2 chu so
# Goi y: C = (F-32)/1.8 va F = 32 + 1.8C
# Vi du: Nhap vao 45F = 7.22C hoac Nhap vao 60C = 140F

nhietdo = raw_input("Nhiet do chuyen doi (eg: 60C, 45F,...): ")
degree = nhietdo[-1];
nhietdo = int(nhietdo[:-1])

if degree == 'C':
    nhietdoF = round(32 + 1.8*nhietdo, 2)
    print "{}C = {}F".format(nhietdo, nhietdoF)
elif degree == 'F':
    nhietdoC = round((nhietdo-32)/1.8, 2)
    print "{}F = {}C".format(nhietdo, nhietdoC)
else:
    print "Nhap sai don vi! Nhap lai"