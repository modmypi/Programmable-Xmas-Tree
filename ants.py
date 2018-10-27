from christmastree import ChristmasTree
from time import sleep

tree = ChristmasTree()

try:
	leds = tree.leds
	while True:
	    for led in leds:
		    led.on()
		    sleep(.2)
		    led.off()
except:
	tree.close()