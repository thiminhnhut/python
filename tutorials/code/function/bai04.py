#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai04.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh dao nguoc cac phan tu trong chuoi

def revstring(s):
    """Function: Dao nguoc cac phan tu trong chuoi"""
    revs = ''
    for i in range(len(s), 0, -1):
        revs = revs + s[i-1]
    return revs

text = '1234abcd'
text_rev = revstring(text)
print "Chuoi dao nguoc cua chuoi {} la {}".format(text, text_rev)