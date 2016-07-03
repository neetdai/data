#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

# 队列:有先进先出的特性
# 就是说先进入队列的节点,获取的时候就会优先出来

class Queue (object):

	def __init__ (self):
		self.__head = None
		self.__tail = None
		self.__length = 0

	# 将节点放进队列中
	def Push (self,node):
		if self.__head == None:
			self.__head = node
			self.__tail = self.__head
		else:
			self.__tail.SetNext(node)
			self.__tail = node
		self.__length += 1

	# 根据先进先出的原则,节点应该从头部获取,
	# 然后将头部节点删除,将头部的指针向后移
	def Pop (self):
		node = self.__head

		if self.__head != None:
			self.__head = self.__head.GetNext()
			node.SetNext(None)

		self.__length -= 1
		return node