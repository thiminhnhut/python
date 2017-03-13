#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai02.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/list/
# Yeu cau:
# Viet chuong trinh con tinh tich cac phan tu trong list

def mullist(lst):
    """
    Tham so lst: list
    Ket qua: Tich cac phan tu trong list
    """
    m = 1   # Gia tri khoi tao
    for i in lst:
        m = m*i   # Nhan don cac phan tu
    return m

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print mullist(x)    # Tinh tich cac phan tu trong list

