#!/usr/bin/python

from openedWindows import *

class AddRecWindow:
	def __init__(self, linkedList, lboxlist):
		self.lboxlist = lboxlist
		self.linkedList = linkedList

		## создание и размещение главного окна
		self.root = Tk()
		self.root.geometry("250x100+1110+200")
		self.root.title("Adding Record")
		self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
		self.root.resizable(width=False, height=False)
		
		## создание, размещение и назначение полей ввода
		self.etList = [Entry(self.root, width = 40) for i in range(4)]
		a = ["Destination", "Flight Number", "Name", "Date (formatted 'DD.MM.YYYY')"]
		for i in range(4):
				self.etList[i].insert(END, a[i])
				self.etList[i].pack()
				self.etList[i].bind("<Button-1>", lambda a = None, ind = i: self.etList[ind].delete(0, END))
		
		
			## создание, размещение и назначение кнопки добавления
		self.butnList = []
		self.butnList.append(Button(self.root, text = "Add", command = self.saveToList))	
		
		self.butnList[0].pack(side = LEFT)
				
		self.root.mainloop()
		
	def saveToList(self):
		currValue = Record( self.etList[0].get(),
							self.etList[1].get(),
							self.etList[2].get(),
							self.etList[3].get() )
		if( len(currValue.date) == 0 or
			len(currValue.destination) == 0 or
			len(currValue.flightNum) == 0 or
			len(currValue.name) == 0 ):
			mb.showerror(title="ERROR",
						message="     You need to fill all fields!     ")

		elif currValue.isValid() == False:
			mb.showerror(title="ERROR",
						message="          Wrong date format!          ")
		else :
			self.linkedList[0].add(currValue)
			
			self.lboxlist[0].delete(0 , END)
			for i in range(self.linkedList[0].length):
				self.lboxlist[0].insert(END, str(self.linkedList[0][i]))

			OpenedWindows.addRecW = 0
			self.root.destroy()
		
	def decline(self):
		OpenedWindows.addRecW = 0
		self.root.destroy()

	def cleanHints(self, Event):
		for i in self.etList:
			i.delete(0, END)
	
	def disable_event(self):
		OpenedWindows.addRecW = 0
		self.root.destroy()