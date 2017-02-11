#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai10.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-basic-exercises.php
# Yeu cau:
# Viet chuong trinh tinh gia tri cua bieu thuc: n + n^2 + n^3 + ... + n^n , voi n la so nguyen

n = int(raw_input("Nhap vao so nguyen n: "))

def luythua(x, a):
    """Tinh luy thua x^a"""
    lt = 1
    for i in range(a):
        lt = lt*x
    return lt

s = 0
for i in range(n):
    s = s + luythua(n, i+1)

print s
