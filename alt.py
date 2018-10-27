from christmastree import ChristmasTree
from time import sleep

def reds_on(leds):
    for led in [1, 3, 4, 6, 8]:
        leds[led].on()
def greens_on(leds):
    for led in [0, 2, 5, 7, 9]:
        leds[led].on()

tree = ChristmasTree()
tree.star.on()
leds = tree.leds

try:
    tree.star.on()
    while True:
        tree.baubles.off()
        reds_on(leds)
        sleep(.5)
        tree.baubles.off()
        greens_on(leds)
        sleep(.5)
except:
        tree.off()
        tree.close()