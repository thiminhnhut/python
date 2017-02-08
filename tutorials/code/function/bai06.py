#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai06.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh kiem tra mot so co nam trong [a, b] hay khong?

def testrange(n, a, b):
    """Function: Kiem tra mot so n co nam trong [a, b] hay khong?"""
    if n in range(a, b+1):
        print '{} thuoc [{}, {}]'.format(n, a, b)
    else:
        print '{} khong thuoc [{}, {}]'.format(n, a, b)

a = 10
b = 20

n = 15
testrange(n, a, b)

n = -15
testrange(n, a, b)