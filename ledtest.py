import board
import neopixel
import time
from random import randint

twinkles = 1000
max_on = 100
#set variables for the NeoPixel class and assign the class
pin = board.D18
leds = 150
bpp = 3
bright = 1.0
autoWrite = False
color_order = neopixel.RGB

strip = neopixel.NeoPixel(pin, leds, auto_write = autoWrite)
wait = 0.001 #1ms

class twinkling():

	def __init__(self, pos, maxred = 255, maxgreen = 255, maxblue = 255, maxbright = 255, wait = 0, on = 0):
		self.pos = pos
		self.maxred = maxred
		self.maxgreen = maxgreen
		self.maxblue = maxblue
		self.maxbright = maxbright
		self.red = 0
		self.green = 0
		self.blue = 0
		self.bright = 0.0
		self.wait = wait + 1
		self.brightstep = self.maxbright / (self.wait / 2)
		self.on = on
		self.midway = 0
		if self.maxred == self.maxgreen == self.maxblue == 0:
			self.maxred = self.maxgreen = self.maxblue = self.maxbright
		else:
			adjust = maxbright/255
			self.maxred = adjust * self.maxred
			self.maxgreen = adjust * self.maxgreen
			self.maxblue = adjust * self.maxblue
		self.redstep = self.maxred / (self.wait/2)
		self.greenstep = self.maxgreen / (self.wait/2)
		self.bluestep = self.maxblue / (self.wait/2)

	def lightFade(self):
		if self.midway == 0 and self.bright >= self.maxbright:
			self.midway = 1
		if self.midway == 0:
			self.bright += self.brightstep
			self.red += self.redstep
			self.green += self.greenstep
			self.blue += self.bluestep
		else:
			self.bright -= self.brightstep
			self.red -= self.redstep
			self.green -= self.greenstep
			self.blue -= self.bluestep
		if self.bright <= 0.0:
			self.red = self.green = self.blue= self.bright = 0.0
			self.on = 0
		if self.red < 0:
			self.red = 0
		if self.green < 0:
			self.green = 0
		if self.blue < 0:
			self.blue = 0
		if self.red > 255:
			self.red = 255
		if self.green > 255:
			self.green = 255
		if self.blue > 255:
			self.blue = 255

	def onAgain(self, maxred = 255, maxgreen = 255, maxblue = 255, maxbright = 255, wait = 0):
		self.on = 1
		self.maxred = maxred
		self.maxgreen = maxgreen
		self.maxblue = maxblue
		self.wait = wait + 1
		self.maxbright = maxbright
		self.brightstep = self.maxbright//(self.wait/2)
		if self.maxred == self.maxgreen == self.maxblue == 0:
			self.maxred = self.maxgreen = self.maxblue = self.maxbright
		else:
			adjust = maxbright/255
			self.maxred = adjust * self.maxred
			self.maxgreen = adjust * self.maxgreen
			self.maxblue = adjust * self.maxblue
		self.redstep = self.maxred / (self.wait/2)
		self.greenstep = self.maxgreen / (self.wait/2)
		self.bluestep = self.maxblue / (self.wait/2)
		self.midway = 0

def wheel(pos, order = 1):
	#does a color transition from Red to Green to Blue then back to Red
	if pos < 0 or pos > 255:
		a = b = c = 0
	elif pos < 85:
		a = int(pos * 3)
		b = int(255 - pos * 3)
		c = 0
	elif pos < 170:
		pos -= 85
		a = int(255 - pos * 3)
		b = 0
		c = int(pos * 3)
	else:
		pos -= 170
		a = 0
		b = int(pos * 3)
		c = int(255 - pos * 3)
	if order == 1:

		return (a, b, c) if color_order == neopixel.RGB or color_order == neopixel.GRB else (a, b, c, 0)
	else:
		return (c, b, a) if color_order == neopixel.RGB or color_order == neopixel.GRB else (c, b, a, 0)

def blackout():
	color = (0,0,0)
	for i in range(leds):
		strip[i] = color
	strip.show()

def colorFill(color):
	for i in range(leds):
		strip[i] = color
	strip.show()

def colorSlowFill(color, wait):
	for i in range(leds):
		strip[i] = color
		strip.show()
		time.sleep(wait)

#indexType 1 stragith across all leds
#indexType 2 every other led doing cross functions
def ledIndex(leds, i, indexType = 1):
	if indexType == 2:
		if i % 2 == 0:
			return int(i/2)
		else:
			return int(leds//2) - int((i+1)/2)
	else:
		return i

#style 1 all leds one color that cycles
#style 2 rainbow across leds that cycles
#method 1 fades across all leds at once
#method 2 uniformly distributes across all leds
def rainbowCycle(wait, iter = 1, order = 1, method = 1, style = 1, indexType = 1):
	for j in range(256 * iter -1):
		if style == 1:
			strip.fill(wheel(j & 255, order))
		else:
			for i in range(leds):
				if indexType > 1:
					index = ledIndex(leds, i, indexType)
				else:
					index = i
				if method == 1:
					color_index = (index * 256 // leds) + j
				else:
					color_index = index + j
				strip[index] = wheel(color_index & 255, order)
		strip.show()
		time.sleep(wait)

def theaterChase(color, wait, iter = 10):
	for j in range(iter):
		for q in range(3):
			for i in range(0, leds, 3):
				strip[i + q] = color
			strip.show()
			time.sleep(wait)
			for i in range(0, leds, 3):
				strip[i + q] = (0,0,0)

def theaterChaseRainbow(wait, iter = 1, order = 1, method = 2):
	for j in range(256 * iter -1):
		for q in range(3):
			for i in range(0, leds, 3):
				if method == 1:
					color_index = (i * 256 // leds) + j
				else:
					color_index = i + j
				strip[i + q] = wheel(color_index & 255, order)
			strip.show()
			time.sleep(wait)
			for i in range(0, leds, 3):
				strip[i+q] = (0,0,0)

def randColor():
	cycle = randint(0,6)
	a = randint(0,256)
	b = 256 - a
	c = 0

	if cycle == 0:
		return (a,b,c)
	elif cycle == 1:
		return (a,c,b)
	elif cycle == 2:
		return (b,a,c)
	elif cycle == 3:
		return (b,c,a)
	elif cycle == 4:
		return (c,a,b)
	else:
		return (c,b,a)

def twinkle(sleep, twinkles = 1000, max_on = 35, color = (0,0,0)):
	#set for led class objects to be held
	stars = set()
	
	on = 0
	through = 0
	maxOnA = randint(0,max_on)
	maxOnB = randint(0,max_on)
	maxOn = (maxOnA, maxOnB)
	maxState = 0
	#determines if a specific color is selected or random
	colorType = 0
	if color == (0,0,0):
		colorType = 1
	elif color == (255,255,255):
		colorType = 2
	#cycles through the process
	for i in range(twinkles):
		#of lights turning on each cycle
		numOn = randint(0,3)
		#only turns lights on if there are less on than the current max allowed on
		if on < maxOnA:
			#adds lights on
			for j in range(numOn):
				#randomly selects light position, length of time on (need to change variable name wait to something else), the maximum brightness, 
				pos = randint(0,leds -1)
				wait = randint(0,50)
				maxbright = randint(0,128)
				if colorType == 1:
					#random color selected
					color = randColor()
				elif color == 2:
					color = (maxbright,maxbright,maxbright)
				maxred = color[0]
				maxgreen = color[1]
				maxblue = color[2]
				#print(f'{maxred}, {maxgreen}, {maxblue}')
				already = 0
				#checks if the led selected already has an object, checks if it is on or off, if off it turns it on
				for x in stars:
					if x.pos == pos:
						if x.on == 1:
							already = 1
						elif x.on == 0:
							already = 1
							x.onAgain(maxred, maxgreen, maxblue, maxbright, wait)
				#if led has not been turned on yet this turns it on
				if already == 0:
					stars.add(twinkling(pos, maxred, maxgreen, maxblue, maxbright, wait, 1))
		on = 0
		#updates led info for this cycle
		for x in stars:
			if x.on == 1:
				on += 1
				#controls what brightness led is at in any given cycle
				x.lightFade()
				#populates my object parameters to the neopixel object (I know there is probably a better way, but I'm not to that point yet.) 
				strip[x.pos] = (int(x.red), int(x.green), int(x.blue))
		strip.show()
		time.sleep(sleep)
		#clunky method for dealing with if lights need to be added or not.
		if on >= maxOnA and maxState == 0:
			if maxOnA > maxOnB:
				maxOnA = maxOnB
				maxOnB = randint(0, max_on)
				if maxOnB >= maxOnA:
					maxState = 1
			elif maxOnA <= maxOnB:
				maxOnA = maxOnB
				maxOnB = randint(0, max_on)
		if on <= maxOnA and maxState == 1:
			maxOnA = maxOnB
			maxOnB = randint(0, max_on)
			maxState = 0
		
blackout()
twinkle(.001, 2000, 75)
strip.deinit()	
