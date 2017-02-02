#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: isprime.py
# Author: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Chuong trinh: Tim day so nguyen to nho hon N

def isprime(N):
    """Function: Tim day so nguyen to nho hon N"""
    Prime = []
    for i in range(1,N):
        count = 0
        for j in range(1, i+1):
            if i%j == 0:
                count = count + 1   # Tang so uoc len
            if count > 2:   # Hon 2 uoc la khong phai so nguyen to
                break
        if count == 2:  # Dung 2 uoc la so nguyen to
            Prime.append(i)
    return Prime

# Chuong trinh chinh
print isprime(100)