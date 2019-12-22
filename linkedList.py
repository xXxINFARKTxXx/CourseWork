#!/usr/bin/python

	#класс Node для определения элемента списка
class Node:
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next

class LinkedList:

	allLists = []
	
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0
		LinkedList.allLists.append(self)

	def __str__(self):
		if self.first != None:
			current = self.first
			out = 'LinkedList [\n' +str(current.value) +'\n'
			while current.next != None:
				current = current.next
				out += str(current.value) + '\n'
			return out + ']'
		return 'LinkedList []'

	def clear(self):
		self.__init__()

	def add(self, x):
		self.length+=1
		if self.first == None:
			#self.first и self.last будут указывать на одну область памяти
			self.last = self.first = Node(x, None)
		else:
			#здесь, уже на разные, т.к. произошло присваивание
			self.last.next = self.last = Node(x, None)

	def push(self, x):
		self.length+=1
		if self.first == None:
			self.last = self.first = Node(x,None)
		else:
			self.first = Node(x,self.first)

	def insertNth(self,i,x):
		if self.first == None:
			self.last = self.first = Node(x, None)
			return
		if i == 0:
			self.first = Node(x,self.first)
			return
		curr=self.first
		count = 0
		while curr != None:
			count+=1
			if count == i:
				curr.next = Node(x,curr.next)
				if curr.next.next == None:
					self.last = curr.next
				break
			curr = curr.next
		return
	
	def Del(self, i):
		if (self.first == None):
			return
		curr = self.first
		count = 0
		old = None
		if i == 0:
			self.first = self.first.next
			self.length -= 1
			return
		while curr != None:
			if count == i:
				if curr.next == None:
					self.last = curr
				old.next = curr.next
				break
			old = curr  
			curr = curr.next
			count += 1
		self.length -= 1

	def __getitem__(self, key):#поддержка обращения по ключу
		length =0
		current=None
		if self.first != None:
			current = self.first
			while current.next != None:
				if key==length:
					break
				current = current.next
				length +=1
			if key==length: current=current.value
		return current

	def __setitem__(self, key, value):#поддержка изменения значения по ключу
		length = 0
		if self.first != None:
			current = self.first
			while key!=length or current.next != None:
				current = current.next
				length +=1
			if key==length: current.value = value
