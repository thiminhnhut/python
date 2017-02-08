#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai08.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-functions-exercises.php
# Yeu cau:
# Viet chuong trinh loai bo cac phan tu trung trong mot danh sach

def relist(lst):
    """Function: Loai bo cac phan tu trung trong mot danh sach"""
    x = []
    for i in lst:
        if i not in x:
            x.append(i)
    return x

l = [1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 1, 2, 5]
lnew = relist(l)
print "Danh sach da cho {}".format(l)
print "Danh sach moi (loai bo cac phan tu trung nhau): {}".format(lnew)
