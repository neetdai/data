#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

class BinaryTreeNode (object):

	def __init__ (self,key,value):
		if isinstance(key,int):
			self.__key = key
		else:
			raise Exception("key must be Integer")
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

	# 前序遍历
	def Preorder_Traversal (self):
		left = self.__left
		right = self.__right

		print(self.__key,self.__value)
		if left != None:
			left.Preorder_Traversal()

		if right != None:
			right.Preorder_Traversal()

	# 中序遍历
	def Inorder_Traversal (self):
		left = self.__left
		right = self.__right

		if left != None:
			left.Inorder_Traversal()

		print(self.__key,self.__value)

		if right != None:
			right.Inorder_Traversal()

	# 后序遍历
	def Postorder_Traversal (self):
		left = self.__left
		right = self.__right

		if left != None:
			left.Postorder_Traversal()

		if right != None:
			right.Postorder_Traversal()

		print(self.__key,self.__value)