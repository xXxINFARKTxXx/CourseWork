#!/usr/bin/python

import re
from datetime import date 

	#класс Record для определения структуры записи
class Record:
	def __init__(self, d, f, n, dt):
		self.destination = d
		self.flightNum = f
		self.name = n
		self.date = dt ## Шаблон даты DD.MM.YYYY

	def __str__(self):
		out = str(self.destination)+", "+str(self.flightNum)+", "+str(self.name)+", "+str(self.date)
		return out

	def isValid(self):

		if len(self.date) != 10:
			return False

		res = re.findall(r'\d{2}.\d{2}.\d{4}', self.date)
		if len(res) != 1:
			return False

		try:
			res = [int(res[0][0:2:1]), int(res[0][3:5:1]), int(res[0][6:10:1])]
			date(res[2], res[1], res[0])
			return True
		except:
			return False

