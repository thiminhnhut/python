#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai31.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh tinh tuoi cua cho. Biet cach tinh tuoi nhu sau:
# + 2 nam dau, tuoi cua cho bang 10.5 nam tuoi cua nguoi.
# + Cac nam sau, 1 nam tuoi cua cho bang 4 nam tuoi cua nguoi.
# Vi du: 15 nam trong tuoi cua nguoi -->73 nam trong tuoi cua cho.

tuoi = float(raw_input("Nhap vao so nam trong tuoi cua nguoi: "))

if tuoi <= 2:
    tuoicho = tuoi * 10.5
else:
    tuoicho = 2*10.5 + (tuoi - 2)*4

print "So tuoi cua cho trong nam cua cho la: {}".format(tuoicho)
