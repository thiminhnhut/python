#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai06.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh dem co bao nhieu so chan, bao nhieu so le trong tuple.
# Vi du: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# So chan: 4 so. So le: 5 so

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = even = 0
for i in numbers:
    if i%2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print "So chan: {} so. So le: {} so".format(even, odd)

