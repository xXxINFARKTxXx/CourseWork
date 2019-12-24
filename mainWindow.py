#!/usr/bin/python

from openedWindows import *
from addRecWindow import AddRecWindow
from filterWindow import FilterWindow

class MainWindow:

	def __init__(self):
		self.linkedList = [LinkedList()]

			# создание главного окна
		self.root = Tk()
		self.root.geometry("710x530+400+200")
		self.root.title("Заявки на авиабилеты")
		self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
		self.root.resizable(width=False, height=False)

			#FRAMES
		self.f_left = Frame(self.root, bd = 3, background = "blue", relief = RIDGE)
		self.f_right = Frame(self.root, bd = 3, background = "blue", relief = RIDGE)

			#BUTTTONS создание органов управления
		self.addRecButn = Button(self.f_left,
						text = "Добавить\n запись",
						width = 13,
						height = 5,
						font = "Arial 12",
						command = self.addRec)

		self.delButnButn = Button(self.f_left,
						text = "Удалить\n выбранную\n запись",
						width = 13,
						height = 5,
						font = "Arial 12",
						command = self.delRec)

		self.showAllRecsButn = Button(self.f_left,
						text = "Показать\n все\n записи",
						width = 13,
						height = 5,
						font = "Arial 12",
						command = self.showAllRecs)

		self.showFilteredRecsButn = Button(self.f_left,
							text = "Фильтр\n записей",
							width = 13,
							height = 5,
							font = "Arial 12",
							command = self.showFilteredRecs)
		
		self.cleanRecsButn = Button(self.f_left,
							text = "Удалить\n все\n записи",
							width = 13,
							height = 5,
							font = "Arial 12",
							command = self.cleanRecs)

		self.scrollbar = Scrollbar(self.f_right,
								width = 16)

			# создание окна списоков записей
		self.lbox = Listbox(self.f_right,
						yscrollcommand = self.scrollbar.set,
						width = 50,
						height = 38,
						font = "Arial 15")
		self.lboxlist = [self.lbox]

			# упаковка всех объектов
		self.f_left.pack(side = LEFT)
		self.f_right.pack(side = LEFT)
		self.addRecButn.pack()
		self.delButnButn.pack()
		self.showAllRecsButn.pack()
		self.showFilteredRecsButn.pack()
		self.cleanRecsButn.pack()
		self.lbox.pack(side = LEFT)
		self.scrollbar.pack(side = LEFT, fill = Y)
		self.scrollbar.config(command = self.lbox.yview)

		self.root.mainloop()
	
	    # функция добавления записи
	def addRec(self):
		if OpenedWindows.addRecW == 0:
			OpenedWindows.addRecW = 1
			AddRecWindow(self.linkedList, self.lboxlist)
			self.showAllRecs()
	
		# функция удаления записи
	def delRec(self):
		a = self.lbox.curselection()
		if(len(a) > 0):
			self.linkedList[0].Del(a[0])
			self.showAllRecs()
	
		# функция показа всех записей в окне
	def showAllRecs(self):
			self.lbox.delete(0 , END)
			for i in range(self.linkedList[0].length):
				self.lbox.insert(END, str(self.linkedList[0][i]))
	
		# функция фильтрации записей
	def showFilteredRecs(self):				
			if OpenedWindows.filterW == 0:
				OpenedWindows.filterW = 1
				FilterWindow(self.linkedList, self.lboxlist)

		# функция удаления всех записей
	def cleanRecs(self):
			self.linkedList[0].clear()
			self.showAllRecs()

		# функция выхода из приложения
	def disable_event(self):
		self.root.destroy()
		
if __name__ == "__main__":
	MainWindow()
