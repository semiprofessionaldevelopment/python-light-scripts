#!/usr/bin/env python

import time
from gpiozero import Button
from mote import Mote

# Added functionality with GPIO buttons 17, 22, 23, and 27.
# Added functionality to extend to second mote hub.
# On user input, this program mutates red, green, and blue values in rgblist and sends them to the buffer (ie. outputs the light colours to the mote LED sticks). The light remains on until another selection is made of the program ends.

# button definition
b17 = Button(17)
b22 = Button(22)
b23 = Button(23)
b27 = Button(27)

# Default RGB definitions (ie. off)
R = 0
G = 0
B = 0
rgblist = [R, G, B]
brightlist = [R, G, B]

#mote definitions: this script allows for multiple Mote controllers. ls /dev/ to determine the names of your more serial ports and plug them in below.
mote = Mote(port_name='/dev/ttyACM0')
mote2 = Mote(port_name='/dev/ttyACM1')
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)
mote2.configure_channel(1, 16, False)
mote2.configure_channel(2, 16, False)
mote2.configure_channel(3, 16, False)
mote2.configure_channel(4, 16, False)
mote.clear()
mote2.clear()

# Light mode name and RGB code for each (2000, 2700, 3000, 3700, 5000 Kelvin)
candle = [255, 138, 18]
fortyw = [255, 169, 87]
hundredw = [255, 180, 107]
halogen = [255, 201, 148]
carbon = [255, 228, 206]

# Brightness lists
off = [0, 0, 0]
quarter = [51, 51, 51]
half = [102, 102, 102]
threequarter = [204, 204, 204]
full = [255, 255, 255]

# main loop
while True:
    # Button 17 cycles thorugh light warmth
    if b17.is_pressed and rgblist == off:
        rgblist = candle
    elif b17.is_pressed and rgblist == candle:
        rgblist = fortyw
    elif b17.is_pressed and rgblist == fortyw:
        rgblist = hundredw
    elif b17.is_pressed and rgblist == hundredw:
        rgblist = halogen
    elif b17.is_pressed and rgblist == halogen:
        rgblist = carbon
    elif b17.is_pressed and rgblist == carbon:
        rgblist = off
    
    # Button 22 cycles through brightness
    elif b22.is_pressed and brightlist == off:
        brightlist = quarter
    elif b22.is_pressed and brightlist == quarter:
        brightlist = half
    elif b22.is_pressed and brightlist == half:
        brightlist = threequarter
    elif b22.is_pressed and brightlist == threequarter:
        brightlist = full
    elif b22.is_pressed and brightlist == full:
        brightlist = off

    mote.clear()
    mote2.clear()
    mote.set_all(rgblist[0], rgblist[1], rgblist[2])
    mote2.set_all(brightlist[0], brightlist[1], brightlist[2])
    mote.show()
    mote2.show()
    time.sleep(0.1)
