#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

from Queue import Queue
from QueueNode import QueueNode

if __name__ == '__main__':
	n1 = QueueNode(0)
	n2 = QueueNode("hello")

	q = Queue()
	q.Push(n1)
	q.Push(n2)

	print(q.Pop().GetValue())
	print(q.Pop().GetValue())
	print(q.Pop())