def stepCalc(value, cycle):
	return value / (cycle / 2)

def colorMaxInit(maxColor, maxBright):
	(maxBright/255) * maxColor

class ledInfo():

	#maxcolor is the most saturated pixel will get
	#color is the current color state of a pixel
	#both = (red, green, blue, brightness)
	def __init__(self, pos, maxcolor = (0,0,0,0.0), onOffCycle = 0, on = 0):
		self.pos = pos
		self.maxcolor = maxcolor
		self.color = (0,0,0,0.0)
		self.onOffCycle = onOffCycle + 1 #prevent /0
		self.step = (0.0,0.0,0.0,0.0)
		self.on = on
		self.midway = 0
		if self.maxcolor[0] == self.maxcolor[1] == self.maxcolor[2] == 0:
			self.maxcolor[0] = self.maxcolor[1] = self.maxcolor[2] = self.maxcolor[3]
		else:
			for i in range(2):
				self.maxcolor[i] = colorMaxInit(self.maxcolor[i], self.maxcolor[3]
		for i in range(3):
			self.step[i] = stepCalc(self.color[i],self.onOffCycle)
		
	def lightFade(self):
		if self.midway == 0 and self.color[3] >= self.maxcolor[3]:
			self.midway = 1
		if self.midway == 0:
			for i in range(3):
				self.color[i] += self.step[i]
		else:
			for i in range(3):
				self.color[i] -= self.step[i]
		if self.color[3] <= 0.0:
			self.color[0] = self.color[1] = self.color[2]= self.color[3] = 0.0
			self.on = 0
		for i in range(2):			
			if self.color[i] < 0:
				self.color[i] = 0
			if self.color[i] > 255:
				self.color[i] = 255

	def onAgain(self, maxcolor = (0,0,0,0.0), onOffCycle = 0):
		self.on = 1
		for i in range(3):
			self.maxcolor[i] = maxcolor[i]
		self.onOffCycle = onOffCycle + 1
		if self.maxcolor[0] == self.maxcolor[1] == self.maxcolor[2] == 0:
			self.maxcolor[0] = self.maxcolor[1] = self.maxcolor[2] = self.maxcolor[3]
		else:
			for i in range(2):
				self.maxcolor[i] = colorMaxInit(self.maxcolor[i], self.maxcolor[3]
		for i in range(3):
			self.step[i] = stepCalc(self.color[i],self.onOffCycle)
		self.midway = 0
