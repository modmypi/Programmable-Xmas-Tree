# Programmable Christmas Tree - Sample Code

![alt text](https://github.com/modmypi/Programmable-Xmas-Tree/blob/master/github_christmastree.png "Christmas Tree")

Here you will find four different code examples to get you started with the [Christmas Tree Solder kit](https://www.modmypi.com/raspberry-pi/led-displays-and-drivers-1034/led-boards-1040/christmas-tree-solder-kit) and the [Programmable Christmas Tree](https://www.modmypi.com/raspberry-pi/led-displays-and-drivers-1034/led-boards-1040/christmas-tree-programmable-kit) from ModMyPi along with a GPIO Zero compatible class extension to easily build your own light shows.

### all_on.py

As the name of the file implies, this simply turns on all the LEDS on the board.

### alt.py

This script will alternate the green leds and red leds. The top white led is allways on.

### ants.py

This script simply turns each led on then off in sequence.

### christmastree.py

The [GPIO Zero](https://github.com/RPi-Distro/python-gpiozero) based class which can be used for building your own LED operations.

### random_leds.py

This script will randomly pulse all LEDs on the board.

## Download and Run

To download the sample code simply run the following command:

```
git clone https://github.com/modmypi/Programmable-Xmas-Tree/
```

To run the sample code:

```
cd Programmable-Xmas-Tree
```

```
sudo python ants.py
```
