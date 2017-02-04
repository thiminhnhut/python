#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai09.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh in ra day so Fibonacci tu 0 - 50.
# Vi du: 1 1 2 3 5 8 13 21 34

n = 50
Fibo = []
a, b = 0, 1
while b < n:
    Fibo.append(b)
    a, b = b, a+b

print Fibo