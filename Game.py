from Tkinter import *
from Cell import *
import random

import time

class Game(Frame):

	def __init__(self, n, dt=100):



		self.n = n
		self.dt = dt

		self.pause = False

		self.root = Tk()

		Frame.__init__(self, None, [])

		self.cells = []

		self.draw(init=True)


	def draw(self, init=False):

		if init:
			self.root.wm_title("Game of Life")
			self.root.geometry("%dx%d" % (600, 600))

			self.width = 500
			self.height = 500

			self.canvas = Canvas(self.root, bg="white")

			self.root.bind("<Configure>", self.resize)

			self.root.bind("<Key>", self.handleKey)

			# add cells
			for y in range(self.n):
				for x in range(self.n):
					self.cells.append(Cell(self, pos=(x,y)))

			for c in self.cells:
				c.initNeighbours()

			self.root.update()

			self.resize()

	def resize(self, event=[]):
		

		self.width=self.root.winfo_width()
		self.height=self.root.winfo_height()

		self.canvas.place(x=0, y=0, width=self.width, height=self.height)

		
		for c in self.cells:
			c.resize()

	def handleKey(self, event=[]):

		key =event.keysym
		print(event.keysym)

		if key=="p":
			if self.pause:
				self.pause = False
				self.step()
				print("UNPAUSE")
			else:
				self.pause = True
				print("PAUSE")

		elif key == "c": # clear
			for c in self.cells:
				c.clear(hard=False)
			print("CLEAR")
		elif key == "C": # clear
			for c in self.cells:
				c.clear(hard=True)
			print("CLEAR")
		elif key == "r": # random
			for c in self.cells:
				c.value = random.random()
				c.draw()
			print("RANDOM")
		elif key == "f": # random
			self.dt *= 0.75
			print("FASTER")
		elif key == "s": # random
			self.dt *= 1./0.75
			print("SLOWER")


	def getCellByPos(self, pos):

		#try:
		return self.cells[pos[0] + pos[1]*self.n]
		#except:
		#	print("ERROR: cell at ", pos, " does not exist")
		#	exit()

	def step(self):

		if self.pause: return

		t0 = time.time()

		for c in self.cells:
			c.getNextValue()


		t1 = time.time()


		for c in self.cells:
			c.update()


		self.after(int(self.dt*1000), self.step)

	def run(self):

		

		self.step()

		self.root.mainloop()

