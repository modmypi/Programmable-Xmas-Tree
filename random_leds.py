from christmastree import ChristmasTree
from gpiozero.tools import random_values
from signal import pause

tree = ChristmasTree(pwm=True)
leds = tree.leds

try:
	for led in leds:
		led.source_delay = 0.1
		led.source = random_values()
	pause()
except KeyboardInterrupt:
	tree.close()