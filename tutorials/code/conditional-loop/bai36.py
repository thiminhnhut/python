#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai36.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh kiem tra tam giac can, tam giac deu va tam giac thuong.
# Cac canh duoc nguoi dung nhap

a = float(raw_input("Canh 1: "))
b = float(raw_input("Canh 2: "))
c = float(raw_input("Canh 3: "))

if a*b*c > 0:
    if a+b > c and a+c > b and b+c > a:
        if a == b and b == c:
            print "Ba canh \t {} \t {} \t {} \t tao thanh tam giac deu".format(a, b, c)
        elif a == b or b == c or a == c:
            print "Ba canh \t {} \t {} \t {} \t tao thanh tam giac can".format(a, b, c)
        else:
            print "Ba canh \t {} \t {} \t {} \t tao thanh tam giac thuong".format(a, b, c)
    else:
        print "Ba canh \t {} \t {} \t {} \t khong tao thanh tam giac".format(a, b, c)
else:
    print "Ban da nhap do dai am"