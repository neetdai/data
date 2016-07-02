#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

from LinkedList import LinkedList

if __name__ == '__main__':
	
	l1 = LinkedList("hello")
	l1.Link(LinkedList("world"))
	l1.Link(LinkedList("aaa"))

	print(l1.Get(2))