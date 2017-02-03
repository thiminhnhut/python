#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: separate.py
# Author: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Chuong trinh: Trich xuat mot tu trong mot file va luu vao file moi

handle = open("definecolorrgb.sty")
g = open("color.txt", "w")

for line in handle:
    line = line.strip() # Loai bo ky tu space
    # Lay mau tu trong moi dong
    # Vi du: line = \definecolor{airforceblue}{rgb}{0.36, 0.54, 0.66}
    # ---> Lay ra: airforceblue ghi vao file
    color = line[line.find("{")+1 : line.find("}")]
    g.write(color + "\n")
g.close()
handle.close()