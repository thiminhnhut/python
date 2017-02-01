# Cập nhật các gói lệnh được cài đặt bằng pip trong Python

Sưu tầm: Thi Minh Nhựt - Email: thiminhnhut@gmail.com

Thời gian: Ngày 01 tháng 02 năm 2017

## Nguồn tham khảo

[Upgrading all packages with pip](https://goo.gl/7T2Tz) trong [Stack Overflow](http://stackoverflow.com/)

## Cách thực hiện

* Nếu bạn muốn cập nhật phiên bản mới cho các gói lệnh được cài đặt bằng `pip` trong Python, 
thực hiện script sau:

		#!/usr/bin/python
		
		# Script: upgrate-package-python.py
		
		# Noi dung: Cap nhat cac goi lenh duoc cai dat bang pip trong Python
		
		
		import pip
		
		from subprocess import call

		
		for dist in pip.get_installed_distributions():
			
			call("pip install --upgrade " + dist.project_name, shell=True)

* Nội dung của script `upgrate-package-python.py`: [Download](https://github.com/thiminhnhut/python/tree/master/tips/upgrate-package-python/upgrate-package-python.py)

* Thực thi script  `upgrate-package-python.py`, các gói lệnh sẽ được cập nhật phiên bản mới.

		sudo python upgrate-package-python.py
