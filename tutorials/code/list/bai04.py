#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai03.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/list/
# Yeu cau:
# Viet chuong trinh con tim so nho nhat trong list

def minlist(lst):
    """
    Tham so lst: list
    Ket qua: So nho nhat trong list
    """
    minlst = lst[0]     # So nho nhat duoc gan bang phan tu dau tien

    # Lay phan tu dau tien di so sanh voi cac phan tu con lai va cap nhat gia tri moi
    for i in lst:
        if i < minlst:
            minlst = i

    return minlst

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [100, 2200, -33, -1000, 5, 6, 777, 8, 9, 90]

# Ham do nguoi dung dinh nghia
print minlist(x)    # Tim phan tu nho nhat trong list
print minlist(y)

# Ham duoc xay dung san
print min(x)    # Tim phan tu nho nhat trong list
print min(y)