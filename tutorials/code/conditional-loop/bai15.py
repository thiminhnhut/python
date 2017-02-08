#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai15.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh kiem tra tinh hop le cua mat khau do nguoi dung nhap vao. Cho biet,
# Mat khau duoc goi la hop le neu:
# + Co it nhat 1 ky tu [a-z] va 1 ky tu tu [A-Z]
# + Co it nhat 1 so tu [0-9]
# + Co it nhat 1 ky tu [$#@]
# + Do dai toi thieu la 6 ky tu va do dai toi da la 16 ky tu

password = raw_input("Moi ban nhap vao mat khau: ")

if len(password) >= 6 and len(password) <= 16:
    count = 0
    for i in password:
        if ord(i) in range(97,123): # [a-z] = [97-122]
            count = count + 1
            break

    for i in password:
        if ord(i) in range(65,91): # [A-Z] = [65-90]
            count = count + 1
            break

    for i in password:
        if ord(i) in [ord('#'), ord('@'), ord('$')]:
            count = count + 1
            break

    for i in password:
        if ord(i) in range(48,58): # [0-9] = [48-57]
            count = count + 1
            break

    if count == 4:
        print "Mat khau hop le!"
    else:
        print "Mat khau khong hop le!"
else:
    print "Mat khau co chieu dai khong hop le!"
