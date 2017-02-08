#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai10.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh in ra cac so chan trong mot danh sach

def evenlist(lst):
    """Function: Tim ra cac so chan trong mot danh sach"""
    even = []
    for i in lst:
        if i%2 == 0:
            even.append(i)
    return even

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sochan = evenlist(a)
print "Danh sach da cho {}".format(a)
print "Danh sach cac so chan {}".format(sochan)