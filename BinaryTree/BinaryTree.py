#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

class BinaryTree (object):

	def __init__ (self):
		self.__head = None
		self.__current = None

	def Insert(self,node):
		self.__current = self.__head
		if self.__head == None:
			self.__head = node
			self.__current = node
		else:
			while True:
				if self.__current.GetKey() > node.GetKey():
					if self.__current.GetLeft() != None:
						self.__current = self.__current.GetLeft()
					else:
						node.SetParent(self.__current)
						self.__current.SetLeft(node)
						break
				elif self.__current.GetKey() < node.GetKey():
					if self.__current.GetRight() != None:
						self.__current = self.__current.GetRight()
					else:
						node.SetParent(self.__current)
						self.__current.SetRight(node)
						break
				else:
					self.__current.Increase()
					break

	def Search (self,key):
		self.__current = self.__head
		while self.__current != None:
			if self.__current.GetKey() == key:
				return True,self.__current
			elif self.__current.GetKey() < key:
				self.__current = self.__current.GetRight()
			else:
				self.__current = self.__current.GetLeft()
		return False,None