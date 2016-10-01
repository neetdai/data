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

	def Remove (self,key):
		exists,node = self.Search(key)
		if exists == True:
			
			parent = node.GetParent()
			left = node.GetLeft()
			right = node.GetRight()

			if parent.GetLeft() is node:
				parent.SetLeft(None)
			else:
				parent.SetRight(None)

			node.SetParent(None)

			if left != None:
				self.Insert(left)
			if right != None:
				self.Insert(right)

	def Preorder_Traversal (self):
		self.__current = self.__head
		if self.__current != None:
			self.__current.Preorder_Traversal()

	def Postorder_Traversal (self):
		self.__current = self.__head
		if self.__current != None:
			self.__current.Postorder_Traversal()

	def Inorder_Traversal (self):
		self.__current = self.__head
		if self.__current != None:
			self.__current.Inorder_Traversal()