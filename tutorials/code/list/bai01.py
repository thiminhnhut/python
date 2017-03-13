#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai01.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/list/
# Yeu cau:
# Viet chuong trinh con tinh tong cac phan tu trong list

def sumlist(lst):
    """
    Tham so lst: list
    Ket qua: Tong cac phan tu trong list
    """
    s = 0   # Gia tri khoi tao
    for i in lst:
        s = s + i   # Cong don cac phan tu
    return s

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tinh tong cac phan tu trong mot list
print sumlist(x)    # Ham do nguoi dung xay dung

print sum(x)    # Ham duoc xay dung san

