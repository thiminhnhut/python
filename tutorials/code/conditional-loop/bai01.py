#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai01.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Tim nhung so vua chia het cho 7 va la boi cua 5, biet cac so nay trong doan [1500, 2700].

# Doan [a, b] can tim
a = 1500
b = 2700

N=[]    # list dung luu tru cac so thoa dieu kien
for i in range(a, b+1): # b+1: do lay gia tri o cac dau mut
    # Dieu kien yeu cau
    # Hoac dung dieu khien: i%35 == 0 --> chia het cho 7 va cho 5
    # if i%35 == 0:
    if i%7 == 0 and i%5 == 0:
        N.append(i)     # Luu lai ket qua

# Xuat ket qua
print N, len(N)