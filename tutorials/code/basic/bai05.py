#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai05.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-basic-exercises.php
# Yeu cau:
# Viet chuong trinh cho phep nguoi dung nhap vao first name va last name.
# In ra thong bao: Hello Last name First name

first_name = raw_input("First name: ")
last_name = raw_input("Last name: ")

print "Hello {} {}".format(last_name, first_name)