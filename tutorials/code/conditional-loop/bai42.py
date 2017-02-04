#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai42.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh tinh tong va trung binh cua n so nguyen duoc nhap tu ban phim.
# Nhap 0 de ket thuc.

ni = -1 # Khoi tao, gia tri tuy y
count = -1  # Tru ra so 0 - so ket thuc
tong = 0.0  # Gan so thuc de chia lay duoc phan thap phan
while ni != 0:
    ni = int(input(""))
    tong = tong + ni
    count = count + 1

average = tong/count
print "Tong cua {} so nguyen la: {} va trung binh cong la: {}".format(count, tong, average)