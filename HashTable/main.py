#! python3
# -*- coding: utf-8 -*-
__author__ = "neet"

from HashTable import HashTable
import random
import time

if __name__ == '__main__':
	h = HashTable(16)
	h["sdf"] = 5
	h[564] = 78
	h["dgerg"] = "a"
	print(h["sdf"])
	print(h[564])
	print(h["dgerg"])
