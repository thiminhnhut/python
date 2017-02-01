#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: fibonacci.py
# Author: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Chuong trinh: Tim day so Fibonacci nho hon N

def fibonacci(N):
    """Function: Tim day so Fibonacci nho hon N"""
    Fibo = []
    a, b = 0, 1
    while b < N:
        Fibo.append(b)
        a, b = b, a+b
    return Fibo

# Chuong trinh chinh
print fibonacci(100)
