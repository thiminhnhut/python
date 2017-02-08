#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai07.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh dem so tu viet hoa va so tu viet thuong trong chuoi

def cupper_lower(s):
    """Function: Dem so tu viet hoa va so tu viet thuong trong chuoi"""
    count_upper = count_lower = 0
    for c in s:
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            count_upper = count_upper + 1
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            count_lower = count_lower + 1
    return (count_upper, count_lower)

## Cach lam khac su dung ham isupper()
def cupper_lower2(s):
    """Function: Dem so tu viet hoa va so tu viet thuong trong chuoi"""
    count_upper = count_lower = 0
    for c in s:
        if c.isupper():
            count_upper = count_upper + 1
        if c.islower():
            count_lower = count_lower + 1
    return (count_upper, count_lower)

# Su dung ham tu dinh nghia voi ord
s = "Thi Minh Nhut"
cupper, clower = cupper_lower(s)
print "Upper: {}, Lower: {}".format(cupper, clower)

# Su dung ham isupper va islower
s = "The quick Brow Fox"
cupper, clower = cupper_lower2(s)
print "Upper: {}, Lower: {}".format(cupper, clower)