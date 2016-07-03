#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

class QueueNode (object):

	def __init__ (self,value):
		self.__next = None
		self.__value = value

	def SetNext(self,node):
		self.__next = node

	def GetNext(self):
		return self.__next

	def GetValue(self):
		return self.__value