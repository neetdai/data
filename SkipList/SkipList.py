#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__autho__ = "neet"

import random
from Node import Node

class SkipList (object):

	__slot__ = ["__maxLevel","__head","__tail","__rand"]

	def __init__ (self,maxLevel = 5,rand = 0.25):
		self.__head = Node(0,"")
		self.__tail = Node(255,"")
		self.__maxLevel = maxLevel
		self.__rand = rand

		index = 0
		while index < maxLevel:
			self.__head.level.insert(index,self.__tail)
			index += 1

	def Insert (self,key,value):

		if self.__tail.key <= key:
			self.__tail.key = key + 1

		level = self.__randLevel()		

		node = Node(key,value)

		for index in range(0,level):
			prev = self.__head
			while prev.level[index].key <= key:
				prev = prev.level[index]

			if prev.key == key:
				prev.value = value
				break
			else:
				node.level.append(prev.level[index])
				prev.level[index] = node


	def __randLevel (self):
		l = 1
		while l <= self.__maxLevel and random.random() < self.__rand:
			l += 1
		return l

	def Remove (self,key):
		pass

	def Search (self,key):
		current = self.__head

		currentlevel = self.__maxLevel - 1
		while currentlevel >= 0:
			while current != self.__tail:
				if current.level[currentlevel].key < key:
					current = current.level[currentlevel]
				elif current.level[currentlevel].key == key:
					current = current.level[currentlevel]
					return True,current
				else:
					break

			currentlevel -= 1
		return False,None

	def watch (self):
		current = self.__head
		while current != self.__tail:
			print(current.level,current.key,current.value)
			current = current.level[0]