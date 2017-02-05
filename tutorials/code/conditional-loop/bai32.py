#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai32.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh kiem tra mot so la nguyen am hay phu am.
# Nguyen am gom cac am: ['a', 'e', 'o', 'u', 'i']
# Phu am: Cac am con lai.

word = raw_input("Nhap vao ky tu [a-z]: ")

if word in ['a', 'e', 'o', 'u', 'i']:
    print "{} la nguyen am".format(word)
elif word == 'y':
    print "{} doi khi la nguyen am hoac phu am".format(word)
else:
    print "{} la phu am".format(word)