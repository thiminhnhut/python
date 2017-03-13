#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script: bai05.py
# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Ma nguon cua bai tap:
# http://www.w3resource.com/python-exercises/list/
# Yeu cau:
# Viet chuong trinh con tim so phan tu co dang chuoi trong list thoa dieu kien sau:
# + Chieu dai chuoi >= 2
# + Ky tu dau tien va ket thuc chuoi phai giong nhau
# Vi du: x = ['abc', 'xyz', 'aba', '1221'] thi ket qua la 2 (gom cac phan tu 'aba' va '1221')

def matchworks(lst):
    """
    Tham so lst: list (cac phan tu cua list la chuoi)
    Ket qua: So luong phan tu la chuoi:
        i) Co chieu dai >= 2
        ii) Bat dau va ket thuc bang nhung ky tu giong nhau
    """
    count = 0
    for w in lst:
        if len(w) >= 2 and w[0] == w[-1]:
            count = count + 1

    return count

x = ['abc', 'xyz', 'aba', '1221']
print matchworks(x)

y = ['aa', 'xyzx', 'aba', '1221', 'a']
print matchworks(y)