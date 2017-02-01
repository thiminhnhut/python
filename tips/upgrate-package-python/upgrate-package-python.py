#!/usr/bin/python
# Script: upgrate-package-python.py
# Noi dung: Cap nhat cac goi lenh duoc cai dat bang pip trong Python

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
	call("pip install --upgrade " + dist.project_name, shell=True)
