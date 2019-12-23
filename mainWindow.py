#!/usr/bin/python

from openedWindows import *
from addRecWindow import *
from filterWindow import *

class MainWindow:

	def __init__(self):
		self.linkedList = [LinkedList()]

		self.root = Tk()
		self.root.geometry("750x560+600+200")
		self.root.title("Coursework")
		self.root.protocol("WM_DELETE_WINDOW", self.disable_event)

			#FRAMES
		self.f_left = Frame(self.root, bd = 3, background = "lightgreen", relief = RIDGE)
		self.f_right = Frame(self.root, bd = 3, background = "blue", relief = RIDGE)

			#BUTTTONS
		self.addRecButn = Button(self.f_left,
						text = "Add\n Record",
						width = 13,
						height = 5,
						font = "Arial 12",
						command = self.addRec)
		#self.addRecButn.bind('<Button-1>', lambda : self.addRec(self))

		self.delButnButn = Button(self.f_left,
						text = "Delete\n chosed\n record",
						width = 13,
						height = 5,
						font = "Arial 12",
						command = self.delRec)

		self.showAllRecsButn = Button(self.f_left,
						text = "Show\n all\n records",
						width = 13,
						height = 5,
						font = "Arial 12",
						command = self.showAllRecs)

		self.showFilteredRecsButn = Button(self.f_left,
							text = "Filter\n records",
							width = 13,
							height = 5,
							font = "Arial 12",
							command = self.showFilteredRecs)
		
		self.cleanRecsButn = Button(self.f_left,
							text = "Clean\n all\n records",
							width = 13,
							height = 5,
							font = "Arial 12",
							command = self.cleanRecs)

		self.scrollbar = Scrollbar(self.f_right,
								width = 16)
		self.lbox = Listbox(self.f_right,
						yscrollcommand = self.scrollbar.set,
						width = 50,
						height = 38,
						font = "Arial 15")

		self.f_left.pack(side = LEFT)
		self.f_right.pack(side = RIGHT)
		
		
		self.addRecButn.pack()
		self.delButnButn.pack()
		self.showAllRecsButn.pack()
		self.showFilteredRecsButn.pack()
		self.cleanRecsButn.pack()
		
		self.lbox.pack(side = LEFT)
		self.scrollbar.pack(side = LEFT, fill = Y)
		self.scrollbar.config(command = self.lbox.yview)

		self.lboxlist = [self.lbox]

		self.root.mainloop()
	
	def addRec(self):
		if OpenedWindows.addRecW == 0:
			OpenedWindows.addRecW = 1
			AddRecWindow(self.linkedList, self.lboxlist)
			self.showAllRecs()
	
	def delRec(self):
		a = self.lbox.curselection()
		if(len(a) > 0):
			self.linkedList[0].Del(a[0])
			self.showAllRecs()
	
	def showAllRecs(self):
			self.lbox.delete(0 , END)
			for i in range(self.linkedList[0].length):
				self.lbox.insert(END, str(self.linkedList[0][i]))
	
	def showFilteredRecs(self):				
			if OpenedWindows.filterW == 0:
				OpenedWindows.filterW = 1
				FilterWindow(self.linkedList, self.lboxlist)

	def cleanRecs(self):
			self.linkedList[0].clear()
			self.showAllRecs()

	def disable_event(self):
		self.root.quit()
		
if __name__ == "__main__":
	MainWindow()
