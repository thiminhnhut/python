#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai03.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/list/
# Yeu cau:
# Viet chuong trinh con tim so lon nhat trong list

def maxlist(lst):
    """
    Tham so lst: list
    Ket qua: So lon nhat trong list
    """
    maxlst = lst[0]     # So lon nhat duoc gan bang phan tu dau tien

    # Lay phan tu dau tien di so sanh voi cac phan tu con lai va cap nhat gia tri moi
    for i in lst:
        if i > maxlst:
            maxlst = i

    return maxlst

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [100, 2200, -33, -1000, 5, 6, 777, 8, 9, 90]

# Ham do nguoi dung dinh nghia
print maxlist(x)    # Tim phan tu lon nhat trong list
print maxlist(y)

# Ham duoc xay dung san
print max(x)    # Tim phan tu lon nhat trong list
print max(y)