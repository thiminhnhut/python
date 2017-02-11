#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai07.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-basic-exercises.php
# Yeu cau:
# Viet chuong trinh in ra phan mo rong cua ten file duoc nhap tu ban phim

filename = raw_input("Nhap vao ten file: ")

ind = filename.find(".")
ext = filename[ind+1:]
print "Phan mo rong cua file {} la {}".format(filename, ext)