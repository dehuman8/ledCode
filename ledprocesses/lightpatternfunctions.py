from random import randint

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
		return (a, b, c)
	else:
		return (c, b, a)
		
def ledIndex(pixels, i, indexType = 1):
	#indexType 1 stragith across all pixels
	#indexType 2 every other led doing cross functions
	if indexType == 2:
		if i % 2 == 0:
			return int(i/2)
		else:
			return int(pixels//2) - int((i+1)/2)
	else:
		return i
		
def randColor(maxBright = 255):
	cycle = randint(0,6)
	a = randint(0,256)
	b = 256 - a
	c = 0

	if cycle == 0:
		return [a,b,c,maxBright]
	elif cycle == 1:
		return [a,c,b,maxBright]
	elif cycle == 2:
		return [b,a,c,maxBright]
	elif cycle == 3:
		return [b,c,a,maxBright]
	elif cycle == 4:
		return [c,a,b,maxBright]
	else:
		return [c,b,a,maxBright]

def onOffCheck(numOn, maxOnA, maxOnB, turnOnOffState):
	if turnOnOffState == 1:
		if numOn > maxOnA:
			if maxOnA >= maxOnB:
				return 2
			else:
				return 3
		else:
			return 1
	if turnOnOffState == 0:
		if numOn <= maxOnA:
			if maxOnA <= maxOnB:
				return 3
			else:
				return 2
		else:
			return 0
			
def onOffSwitch(turnOnOffState):
	if turnOnOffState % 2 == 0:
		return 1
	return 0

def pixelsToTurnOn(turnOnOffState):
	#of lights turning on each cycle
	#if the max lights is less than number lit reduces the number of lights 
	#that can come on so it more slowly goes down
	a = randint(0,3)
	if turnOnOffState == 0:
		return a // 3	
	return a

def colorType(color):
	#determines if a specific color is selected or it will be random
	if color != (0,0,0,0.0):
		return 1
	return 0