#!/usr/bin/python

from openedWindows import *

class FilterWindow:
	def __init__(self, linkedList, lboxlist):

			# импорт данных из главного окна
		self.linkedList = linkedList
		self.lboxlist = lboxlist

			# создание окна добавления записи
		self.root = Tk()
		self.root.geometry("250x70+1110+340")
		self.root.title("Фильтр")
		self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
		self.root.resizable(width=False, height=False)

		self.f_top = Frame(self.root)
		self.f_bot = Frame(self.root)

			# создание и назначение окна ввода даты
		self.date = Entry(self.root, width = 40)
		self.date.bind("<Button-1>", lambda a = None : self.date.delete(0, END))

			# создание и назначение окна ввода номера полета
		self.flighNum = Entry(self.root, width = 40)
		self.flighNum.bind("<Button-1>", lambda a = None : self.flighNum.delete(0, END))

			# создание и назначение кнопки фильтрации 
		self.fillterButn = Button(self.root,
									text = "Применить",
									width = 9,
									height = 0,
									font = "Arial 8",
									command = self.filterList)

			# размещение элементов
		self.date.pack()
		self.date.insert(END, "Дата (Формат 'ДД.ММ.ГГГГ')")
		self.flighNum.pack()
		self.flighNum.insert(END, "Рейс №")
		self.fillterButn.pack(side = LEFT)

		self.root.mainloop

		# фильтрация листа
	def filterList(self):
		
		date = self.date.get()
		flightNum = self.flighNum.get()

		if (flightNum == "Рейс №"): flightNum = ""
		if (date == "Дата (Формат 'ДД.ММ.ГГГГ')"): date = ""
		validDate = Record(1,1,1,date)

		if(len(date) == 0 and len(flightNum) == 0):
			mb.showerror(title="ОШИБКА",
						message="      Нужно заполнить хотябы одно поле!      ")

		elif(validDate.isValid() == False and len(date) != 0):
			mb.showerror(title="ОШИБКА",
						message="          Неправильный формат даты!          ")

		else :
			self.lboxlist[0].delete(0 , END)
			for i in range(self.linkedList[0].length):

				if(len(flightNum) != 0 and len(date) != 0):	
					if(self.linkedList[0][i].date == date and self.linkedList[0][i].flightNum == flightNum):
						self.lboxlist[0].insert(END, self.linkedList[0][i])

				elif(len(flightNum) == 0 and len(date) != 0):
					if(self.linkedList[0][i].date == date):
						self.lboxlist[0].insert(END, self.linkedList[0][i])

				elif(len(flightNum) != 0 and len(date) == 0):
					if(self.linkedList[0][i].flightNum == flightNum):
						self.lboxlist[0].insert(END, self.linkedList[0][i])

			OpenedWindows.filterW = 0
			self.root.destroy()

		# функция выхода из окна добавления 
	def disable_event(self):
		OpenedWindows.filterW = 0
		self.root.destroy()
