#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai09.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh kiem tra mot so co phai la so nguyen to hay khong

def isprime(n):
    """Function: Kiem tra mot so co phai la so nguyen to hay khong"""
    if n < 2:
        return False
    else:
        t = True
        for i in range(2, n): # Kiem tra tu 2 - (n-1)
            if n%i == 0:
                t = False
                break
        return t

n = 61
np = isprime(n)
if np:
    print "{} la so nguyen to".format(n)
else:
    print "{} khong la so nguyen to".format(n)


