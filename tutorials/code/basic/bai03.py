#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai03.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/python-basic-exercises.php
# Yeu cau:
# Viet chuong trinh hien thi ngay thang va thoi gian hien tai. Vi du: 2017-02-12 18:02:51

import datetime

now = datetime.datetime.now()
print now.strftime("%Y-%m-%d %H:%M:%S")
