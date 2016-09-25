#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

class BinaryTreeNode (object):

	def __init__ (self,key,value):
		self.__key = key
		self.__value = value
		self.__count = 0
		self.__left = None
		self.__right = None
		self.__parent = None

	def GetKey (self):
		return self.__key

	def GetValue (self):
		return self.__value

	def SetLeft (self,node):
		self.__left = node

	def GetLeft (self):
		return self.__left

	def SetRight (self,node):
		self.__right = node

	def GetRight (self):
		return self.__right

	def SetParent (self,node):
		self.__parent = node

	def GetParent (self):
		return self.__parent

	# 增加
	def Increase (self):
		self.__count += 1

	# 减少
	def Decrease (self):
		self.__count -= 1

	def GetCount (self):
		return self.__count