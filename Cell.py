from Tkinter import *
import random
import math
import copy

class Cell:


	def __init__(self, parent, pos):

		self.on_colour =  [1., 1., 1.] #[1.0,0.5,0.6]#
		self.off_colour = [0., 0., 0.] #[0.65, 1.0, 0.75]   #
		self.fixed_colour = [0, 0, 1.] #[0,0,0] #
		self.border_width = 1 # with of rectangle border (probably want either 0 or 1)

		# how quickly the colour for a cell changes from on colour to off colour
		#   (0.5 means that every fram, the colour moves half-way from current colour to target colour)
		# for normal GOL colours, set this to 1
		self.alive_to_dead_change_rate = 0.05

		# how quickly the colour for a cell changes from off colour to on colour
		# for normal GOL colours, set this to 1
		self.dead_to_alive_change_rate = 0.8
		





		self.parent = parent
		self.pos = pos

		self.value = random.randint(0, 1)
		self.lastUpdate = self.value

		self.fixed = False

		self.colour = self.off_colour

		self.draw(init=True)

	def draw(self, init=False, frac=None):


		if init:
			self.getColour()
			self.rectangle = self.parent.canvas.create_rectangle(0,0,0,0, fill=toHex(self.colour), width=self.border_width)
			self.resize()

			self.parent.canvas.tag_bind(self.rectangle, '<Button-1>', self.click)
			self.parent.canvas.tag_bind(self.rectangle, '<Button-3>', self.fix)

			if self.pos[0] == self.parent.n/2 and self.pos[1] == self.parent.n/2:
				self.parent.canvas.itemconfig(self.rectangle, activefill="green")
			elif self.pos[0] == self.parent.n/2 or self.pos[1] == self.parent.n/2:
				self.parent.canvas.itemconfig(self.rectangle, activefill="red")
			else:
				self.parent.canvas.itemconfig(self.rectangle, activefill="yellow")

		self.getColour(frac=frac)
		self.parent.canvas.itemconfig(self.rectangle, fill=toHex(self.colour))


	def initNeighbours(self):

		self.neighbours = []
		self.neighbourWeights = []

		pos = self.pos
		n = self.parent.n

		nRad = 1
		for x in range(-nRad, nRad+1):
			for y in range(-nRad, nRad+1):
				if x == 0 and y ==0: continue

				#if pos[0]+x >= n or pos[1] + y >= n: continue
				#if pos[0]+x < 0 or pos[1] + y < 0: continue

				p = [(pos[0] + x)%n, (pos[1] + y)%n]

				self.neighbours.append(self.parent.getCellByPos(p))

				dist = (1.*abs(x)**2 + 1.*abs(y)**2)**0.5

				self.neighbourWeights.append(1./(dist*dist))

		return

	def click(self, event=[]):

		#for s in self.neighbours:

		#	self.parent.canvas.itemconfig(s.rectangle, fill="red")

		self.value = (1 - self.value)
		self.draw(frac=1.0)

	def fix(self, event=[]):
		# the cell value at whatever value it is at
		self.fixed = not self.fixed
		self.clear(hard=False)
		self.draw()


	def getNextValue(self):

		if self.fixed:
			self.next = self.value
			return

		nSum = 0

		for N in self.neighbours:

			nSum += N.value


		#if self.value == 1 and nSum < 2:
		if nSum < 2:
			self.next = 0
		elif self.value == 1 and nSum ==2 or nSum == 3:
			self.next = 1
		elif self.value == 1 and nSum > 3:
			self.next = 0
		elif self.value == 0 and nSum == 3:
			self.next = 1
		else:
			self.next = 0
		
		return



	def update(self):

		#if self.value == self.next: return

		self.value = self.next

		self.draw()

		


	def getColour(self, frac=None):

		newColour = self.off_colour

		final_frac = frac

		frac = 1.0

		if not self.fixed:
			if self.value == 0:
				frac = self.alive_to_dead_change_rate
				newColour = self.off_colour
			else:
				frac = self.dead_to_alive_change_rate
				newColour = self.on_colour
		else:
			frac = 1.0
			if self.value == 0:
				newColour = blend(self.off_colour, self.fixed_colour, 0.4)
			else:
				newColour = blend(self.on_colour, self.fixed_colour, 0.4)

		if final_frac != None: frac = final_frac




		self.colour = blend(self.colour, newColour, frac)


	def resize(self):

		scr_width = self.parent.width
		scr_height = self.parent.height

		self.width = 1.*scr_width/self.parent.n
		self.height = 1.*scr_height/self.parent.n

		x = self.pos[0]*self.width
		y = self.pos[1]*self.height



		self.parent.canvas.coords(self.rectangle, x, y, x+self.width, y+self.height)

	def clear(self, hard=False):

		if not hard:
			if self.fixed: return
			self.value = 0
			self.colour = self.off_colour
			self.draw()
		else:
			self.value = 0
			self.fixed=False
			self.colour = self.off_colour
			self.draw()


def blend(C1, C2, frac):
	newC = [v1*(1.-frac) + v2*frac for v1, v2 in zip(C1, C2)]
	return newC

def toHex(cvec):

	rgb = tuple([int(255*v) for v in cvec])

	return '#%02x%02x%02x' % rgb