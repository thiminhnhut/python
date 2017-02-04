#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai10.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Yeu cau:
# Viet chuong trinh in ra thong tin nhu sau:
# + Neu mot so la boi cua 3 --> in ra "Fizz"
# + Neu mot so la boi cua 5 --> in ra "Buzz"
# + Neu mot so la boi cua 3 va 5 --> in ra "FizzBuzz"
# + Neu khong phai 3 truong hop tren thi in ra cac so tuong ung.
# Cho biet cac so trong doan [0,50]

n = 50
for i in range(n+1):
    if i%3 == 0:
        print "Fizz"
        continue
    elif i%5 == 0:
        print "Buzz"
        continue
    elif i%3 == 0 and i%5 == 0:
        print "FizzBuzz"
        continue
    else:
        print i