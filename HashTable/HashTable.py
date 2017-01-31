#! python3
# -*- coding: utf-8 -*-
__author__ = "neet"

import sys

class Entry (object):

	def __init__ (self,key,value):
		self.key = key
		self.value = value
		self.next = None

class HashTable (object):

	def __init__ (self,size):
		self.__size = size
		self.__sizemark = self.__size - 1
		self.__table = [None for _ in range(0,self.__size)]
		self.__used = 0

	# murmurhash3
	def __hash (self,key,seed):
		if isinstance(key,int):
			if key < 0:
				raise ValueError("key unable to less than zero")
			key = key.to_bytes(10,byteorder = sys.byteorder)
		elif isinstance(key,str):
			key = key.encode("utf-8")
		elif isinstance(key,bytes):
			pass
		else:
			raise TypeError("key type error!")
		
		m = 0xc6a4a7935bd1e995
		r = 47

		length = len(key)

		h1 = seed ^ length
		h2 = 0

		data = list(key)

		i = 0

		while length >= 8:
			k1 = data[i]
			i += 1
			k1 *= m
			k1 ^= k1 >> r
			k1 *= m
			h1 *= m
			h1 ^= k1
			length -= 4
			
			k2 = data[i]
			i += 1
			k2 *= m
			k2 ^= k2 >> r
			k2 *= m
			h2 *= m
			h2 ^= k2
			length -= 4

		if length >= 4:
			k1 = data[i]
			i += 1
			k1 *= m
			k1 ^= k1 >> r
			k1 *= m
			h1 *= m
			h1 ^= k1
			length -= 4

		if length == 3:
			h2 ^= data[2] << 16
		elif length == 2:
			h2 ^= data[1] << 8
		elif length == 1:
			h2 ^= data[0]
			h2 *= m

		h1 ^= h2 >> 18
		h1 *= m
		h2 ^= h1 >> 22
		h2 *= m
		h1 ^= h2 >> 17
		h1 *= m
		h2 ^= h1 >> 19
		h2 *= m

		h = h1
		h = (h << 32) | h2
		
		return h

	def __setitem__ (self,key,value):

		h = self.__hash(key,self.__sizemark)
		position = h % self.__sizemark
		
		if self.__table[position] == None:
			self.__table[position] = Entry(key,value)
			self.__used += 1
		else:
			current = self.__table[position]

			while current.key != key and current.next != None:
				current = current.next

			if current.key == key:
				current.value = value
			else:
				e = Entry(key,value)
				e.next = current
				current = e

	def __getitem__ (self,key):
		h = self.__hash(key,self.__sizemark)
		position = h % self.__sizemark
		
		if position < 0 or position >= self.__size:
			return None
		elif self.__table[position] != None:
			current = self.__table[position]
			while current.key != key and current.next != None:
				current = current.next
			if current.key == key:
				return current.value
			else:
				return None