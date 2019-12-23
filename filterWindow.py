#!/usr/bin/python

from openedWindows import *

class FilterWindow:
	def __init__(self, linkedList, lboxlist):

		self.linkedList = linkedList
		self.lboxlist = lboxlist

		self.root = Tk()
		self.root.geometry("300x70+1350+340")
		self.root.title("Filter")
		self.root.protocol("WM_DELETE_WINDOW", self.disable_event)

		self.f_top = Frame(self.root)
		self.f_bot = Frame(self.root)

		self.date = Entry(self.root, width = 40)
		self.date.bind("<Button-1>", self.cleanHints)

		self.flighNum = Entry(self.root, width = 40)
		entry = self.flighNum
		self.flighNum.bind("<Button-1>", self.cleanHints)

		self.fillterButn = Button(self.root,
									text = "Filter List",
									width = 9,
									height = 0,
									font = "Arial 8",
									command = self.filterList)

		self.date.pack()
		self.date.insert(END, "Date (formatted 'DD.MM.YYYY')")
		self.flighNum.pack()
		self.flighNum.insert(END, "Flight Number")
		self.fillterButn.pack(side = LEFT)

		self.root.mainloop

	def filterList(self):
		
		date = self.date.get()
		flightNum = self.flighNum.get()

		if (flightNum == "Flight Number"): flightNum = ""
		if (date == "Date (formatted 'DD.MM.YYYY')"): date = ""
		validDate = Record(1,1,1,date)

		if(len(date) == 0 and len(flightNum) == 0):
			mb.showerror(title="ERROR",
						message="      You need to fill one or all fields!      ")

		elif(validDate.isValid() == False and len(date) != 0):
			mb.showerror(title="ERROR",
						message="          Wrong date format!          ")

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
	
	def cleanHints(self, Event):
		self.date.delete(0, END)
		self.flighNum.delete(0, END)

	def disable_event(self):
		OpenedWindows.filterW = 0
		self.root.destroy()
