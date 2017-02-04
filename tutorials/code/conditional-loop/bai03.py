#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai03.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh doan so tu 0 - 9, su dung ham randint (trong module random)
# + Neu nhap dung: "Well guessed!" --> Thoat chuong trinh.
# + Neu nhap sai: "Try again!" --> Nhap lai cho den khi dung.
# + Dem so lan nhap sai.

import random

count = 0
while True:
    a = int(raw_input("Moi ban chon so [0-9]? "))
    if a == random.randint(0, 9):
        print "Well guessed!"
        print "So lan ban doan sai la {}".format(count)
        break
    else:
        count = count + 1
        print "Try again!"