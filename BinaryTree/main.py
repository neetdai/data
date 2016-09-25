#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

from BinaryTreeNode import BinaryTreeNode
from BinaryTree import BinaryTree

if __name__ == '__main__':
	n1 = BinaryTreeNode(5,"hello")
	n2 = BinaryTreeNode(3,"world")
	n3 = BinaryTreeNode(4,"hi")
	n4 = BinaryTreeNode(6,"bye")

	t = BinaryTree()
	t.Insert(n1)
	t.Insert(n2)
	t.Insert(n3)
	t.Insert(n4)

	print(n1.GetRight().GetKey())
	print(t.Search(4))