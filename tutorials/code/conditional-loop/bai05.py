#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai05.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh nhan vao mot tu vao dao nguoc tu nay lai.
# Vi du: Nhap vao abc --> cbc

word = raw_input("Nhap vao mot tu: ")
w = ""
for i in range(len(word)-1, -1, -1):
    w = w + word[i]
print w