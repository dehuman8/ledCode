import board
import neopixel
from ledprocesses import lightpatterns as lp


twinkles = 500
maxOn = 100
pin = board.D18
pixels = 150
autoWrite = False
pixelstrip = neopixel.NeoPixel(pin, pixels, auto_write = autoWrite)
slower = 0.025 
faster = .001
red = (255,0,0,255)
green = (0,255,0,255)
blue = (0,0,255,255)
colorSet = [150,200,0,255]
#pixelstrip = list()
#for i in range(pixels):
#	pixelstrip.append(i)

if __name__ == '__main__':
	while True:		
		lp.blackout(pixelstrip, pixels)
		lp.colorFill(pixelstrip, pixels, blue)
		lp.blackout(pixelstrip, pixels)
		lp.colorSlowFill(pixelstrip, pixels, green, slower)
		lp.blackout(pixelstrip, pixels)
		lp.twinkle(pixelstrip, pixels, faster, twinkles, maxOn, colorSet)
		lp.blackout(pixelstrip, pixels)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 1, 1, 1, 1)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 2, 1, 1, 1)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 1, 2, 1, 1)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 2, 2, 1, 1)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 1, 1, 2, 1)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 2, 1, 2, 1)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 1, 2, 2, 1)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 2, 2, 2, 1)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 1, 1, 1, 2)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 2, 1, 1, 2)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 1, 2, 1, 2)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 2, 2, 1, 2)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 1, 1, 2, 2)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 2, 1, 2, 2)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 1, 2, 2, 2)
		lp.rainbowCycle(pixelstrip, pixels, faster, 1, 2, 2, 2, 2)
		lp.blackout(pixelstrip, pixels)
		lp.theaterChase(pixelstrip, pixels, red, slower)
		lp.theaterChase(pixelstrip, pixels, green, slower)
		lp.theaterChase(pixelstrip, pixels, blue, slower)
		lp.blackout(pixelstrip, pixels)
		lp.theaterChaseRainbow(pixelstrip, pixels, slower, 1, 1)
		lp.theaterChaseRainbow(pixelstrip, pixels, slower, 1, 2)
		lp.blackout(pixelstrip, pixels)
		lp.twinkle(pixelstrip, pixels, faster, twinkles, maxOn)
		lp.blackout(pixelstrip, pixels)
		break
	pixelstrip.deinit()	
