import time
import ledclass as lc
import lightpatternfunctions as lpf
from random import randint

def blackout(pixelstrip, pixels, wait = 1):
	color = (0,0,0)
	for i in range(pixels):
		pixelstrip[i] = color
	pixelstrip.show()
	time.sleep(wait)

def colorFill(pixelstrip, pixels, color):
	for i in range(pixels):
		pixelstrip[i] = color
	pixelstrip.show()

def colorSlowFill(pixelstrip, pixels, color, wait):
	for i in range(pixels):
		pixelstrip[i] = color
		pixelstrip.show()
		time.sleep(wait)

#style 1 all pixels one color that cycles
#style 2 rainbow across pixels that cycles
#method 1 fades across all pixels at once
#method 2 uniformly distributes across all pixels
def rainbowCycle(pixelsstrip, pixels, wait, iter = 1, order = 1, method = 1, style = 1, indexType = 1):
	for j in range(256 * iter -1):
		if style == 1:
			pixelstrip.fill(lpf.wheel(j & 255, order))
		else:
			for i in range(pixels):
				if indexType > 1:
					index = lpf.ledIndex(pixels, i, indexType)
				else:
					index = i
				if method == 1:
					color_index = (index * 256 // pixels) + j
				else:
					color_index = index + j
				pixelstrip[index] = lpf.wheel(color_index & 255, order)
		pixelstrip.show()
		time.sleep(wait)

def theaterChase(pixelstrip, pixels, color, wait, iter = 10):
	for j in range(iter):
		for q in range(3):
			for i in range(0, pixels, 3):
				pixelstrip[i + q] = (color[0], color[1], color[2])
			pixelstrip.show()
			time.sleep(wait)
			for i in range(0, pixels, 3):
				pixelstrip[i + q] = (0,0,0)

def theaterChaseRainbow(pixelstrip, pixels, wait, iter = 1, order = 1, method = 2):
	for j in range(256 * iter -1):
		for q in range(3):
			for i in range(0, pixels, 3):
				if method == 1:
					color_index = (i * 256 // pixels) + j
				else:
					color_index = i + j
				pixelstrip[i + q] = lpf.wheel(color_index & 255, order)
			pixelstrip.show()
			time.sleep(wait)
			for i in range(0, pixels, 3):
				pixelstrip[i+q] = (0,0,0)

def twinkle(pixelstrip, pixels, wait, twinkles = 1000, maxOn = 35, maxColor = (0,0,0, 0.0)):
	#set for led class objects to be held
	stars = set()
	turnOnOffState = 1
	maxOnA = randint(0,maxOn)
	maxOnB = randint(0,maxOn)
	colorType = lpf.colorType(maxColor)
	#cycles through the process
	for i in range(twinkles):
		numTurnedOn = lpf.pixelsToTurnOn(turnOnOffState)	
		for j in range(numTurnedOn):
			#randomly selects light position, length of time on, the maximum brightness, 
			pos = randint(0,pixels -1)
			onOffCycle = randint(0,50)
			maxBright = randint(0,128)
			if colorType == 0:
				maxColor = lpf.randColor(maxBright)
			already = 0
			#checks if the led selected already has an object, checks if it is on or off, if off it turns it on
			for x in stars:
				if x.pos == pos:
					if x.on == 1:
						already = 1
					elif x.on == 0:
						already = 1
						x.onAgain(maxColor, onOffCycle)
			#if led has not been turned on yet this turns it on
			if already == 0:
				stars.add(lc.ledInfo(pos, maxColor, onOffCycle, 1))
		numOn = 0
		#updates led info for this cycle
		for x in stars:
			if x.on == 1:
				numOn += 1
				#controls what brightness led is at in any given cycle
				x.lightFade()
				#populates my object parameters to the neopixel object (I know there is probably a better way, but I'm not to that point yet.) 
				pixelstrip[x.pos] = (int(x.color[0]), int(x.color[1]), int(x.color[2]))
		pixelstrip.show()
		time.sleep(wait)
		#controlls if lights will be turned on or off
		turnOnOffState = lpf.onOffCheck(numOn, maxOnA, maxOnB, turnOnOffState)
		if turnOnOffState > 1:
			maxOnA = maxOnB
			maxOnB = randint(0, maxOn)
			turnOnOffState = lpf.onOffSwitch(turnOnOffState)
