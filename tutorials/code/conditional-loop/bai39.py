#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai39.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh cho biet ten cua nam duoc nhap vao. Cho biet nam 2000 la Canh Thinh

year = int(raw_input("Nam: "))

#Can = ["Giap", "At", "Binh", "Dinh", "Mau", "Ky", "Canh", "Tan", "Nham", "Quy"]
#Chi = ["Ty", "Suu", "Dan", "Meo", "Thinh", "Ty", "Ngo", "Mui", "Than", "Dau", "Tuat", "Hoi"]

Can = ["Canh", "Tan", "Nham", "Quy", "Giap", "At", "Binh", "Dinh", "Mau", "Ky"]
Chi = ["Thin", "Tyj", "Ngo", "Mui", "Than", "Dau", "Tuat", "Hoi", "Tys", "Suu", "Dan", "Meo"]

if year >= 2000:
    print Can[(year - 2000)%10] + " " + Chi[(year - 2000)%12]
else:
    if year % 10 == 0:
         s = Can[abs((year - 2000))%10]
    else:
        s = Can[10 - abs((year - 2000))%10]
    print s + " " + Chi[12 - abs((year - 2000))%12]
