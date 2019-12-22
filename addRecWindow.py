#!/usr/bin/python

from openedWindows import *

class AddRecWindow:
	def __init__(self, linkedList, lboxlist):
		self.lboxlist = lboxlist
		self.linkedList = linkedList

		self.root = Tk()
		self.root.geometry("300x100+1350+200")
		self.root.title("Adding Record")
		self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
		
		self.etList = []
		a = ["Destination", "Flight Number", "Name", "Date (formatted 'DD.MM.YYYY')"]
		for i in range(4):
				self.etList.append(Entry(self.root, width = 40))
				self.etList[i].insert(END, a[i])
				self.etList[i].pack()
		
		self.butnList = []
		self.butnList.append(Button(self.root, text = "Add"))
		self.butnList[0].bind('<Button-1>', lambda list = self.linkedList: self.saveToList(self.linkedList))
		
		self.butnList.append(Button(self.root, text = "Decline"))
		self.butnList[1].bind('<Button-1>', lambda x = None: self.decline())
		
		for i in range(2):
				self.butnList[i].pack(side = LEFT)
				
		self.root.mainloop()
		
	def saveToList(self, linkedList):
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
	
	def disable_event():
		pass