from christmastree import ChristmasTree
from time import sleep

tree = ChristmasTree()

tree.on()

try:
    while True:
	    sleep(.5)
except:
    tree.off()
    tree.close()
