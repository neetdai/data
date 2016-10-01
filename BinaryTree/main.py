#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "neet"

from BinaryTreeNode import BinaryTreeNode
from BinaryTree import BinaryTree

if __name__ == '__main__':
	n1 = BinaryTreeNode(5,"hello")
	n2 = BinaryTreeNode(3,"world")
	n3 = BinaryTreeNode(4,"hi")
	n4 = BinaryTreeNode(7,"bye")
	n5 = BinaryTreeNode(8,"8")
	n6 = BinaryTreeNode(6,"6")
	n7 = BinaryTreeNode(2,"2")

	t = BinaryTree()
	t.Insert(n1)
	t.Insert(n2)
	t.Insert(n3)
	t.Insert(n4)
	t.Insert(n5)
	t.Insert(n6)
	t.Insert(n7)

	print(n1.GetRight().GetKey())
	print(t.Search(6))
	# t.Remove(3)
	# _,node = t.Search(4)
	# print(node.GetParent().GetKey())
	# t.Preorder_Traversal()
	# t.Inorder_Traversal()
	# t.Postorder_Traversal()