#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

from SkipList import SkipList
import random

if __name__ == '__main__':
	s = SkipList(10,0.25)
	print(s)

	for index in range(1,1000):
		s.Insert(random.randrange(1,1000,1),"sdfgwef")

	
	s.watch()

	print(s.Search(2))

	s.Remove(2)
	print(s.Search(2))
	print(s.Search(3))