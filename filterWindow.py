#!/usr/bin/python

from openedWindows import *

class FilterWindow:
	def __init__(self, linkedList, lboxlist):

		self.linkedList = linkedList
		self.lboxlist = lboxlist

		self.root = Tk()
		self.root.geometry("300x70+1350+340")
		self.root.title("Filter")
		self.root.protocol("WM_DELETE_WINDOW", lambda x = None: self.disable_event())

		self.f_top = Frame(self.root)
		self.f_bot = Frame(self.root)

		self.date = Entry(self.root, width = 40)
		self.flighNum = Entry(self.root, width = 40)

		self.fillterButn = Button(self.root,
									text = "Filter List",
									width = 9,
									height = 0,
									font = "Arial 8",
									command = self.filterList)

		self.declineButn = Button(self.root, text = "Decline")
		self.declineButn.bind('<Button-1>', lambda x = None: self.decline())

		self.date.pack()
		self.date.insert(END, "Date (formatted 'DD.MM.YYYY')")
		self.flighNum.pack()
		self.flighNum.insert(END, "Flight Number")
		self.fillterButn.pack(side = LEFT)
		self.declineButn.pack(side = LEFT)

		self.root.mainloop

	def filterList(self):
		self.lboxlist[0].delete(0 , END)

		date = self.date.get()
		flightNum = self.flighNum.get()

		if(len(date) == 0 or len(flightNum) == 0):
			mb.showerror(title="ERROR",
						message="      You need to fill all fields!      ")
		
		validDate = Record(1,1,1,date)
		if(validDate.isValid() == False):
			mb.showerror(title="ERROR",
						message="          Wrong date format!          ")
		else :
			for i in range(self.linkedList[0].length):
				if(self.linkedList[0][i].date == date and
					self.linkedList[0][i].flightNum == flightNum):
					self.lboxlist[0].insert(END, self.linkedList[0][i])

			OpenedWindows.filterW = 0
			self.root.destroy()
	
	def decline(self):
		OpenedWindows.filterW = 0
		self.root.destroy()

	def disable_event():
		pass
