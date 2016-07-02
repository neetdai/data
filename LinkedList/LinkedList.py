#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

# 可能是最简单的链表结构吧
# 我认为一个链表最基本有的功能应该是 连接
class LinkedList (object):
	
	# 这是链表的节点
	def __init__ (self,value):
		self.__next = None
		self.__value = value

	# 连接 将新的节点连接到链表的尾部
	def Link (self,node):
		tail = self
		while tail.__next != None:
			tail = tail.__next
		tail.__next = node

	# 得到第几个节点
	def Get (self,index):
		i = 0
		current = self
		# 如果节点的位置超过链表的长度,则返回False
		while i < index and current.__next != None:
			current = current.__next
			i += 1
		if i != index:
			return False,None
		else:
			return True,current.__value
