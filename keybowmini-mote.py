#!/usr/bin/env python

import time
from mote import Mote
import keybow

# On user input, this program mutates red, gree, and blue values in rgblist and sends them to the buffer (ie. outputs the light colours to the mote LED sticks). The light remains on until another selection is made of the program ends.

# start keybow mini 
keybow.setup(keybow.MINI)

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

# when pressed, keybow buttons cycle through the RGB light colour lists.
@keybow.on(index=0)
def handle_key(index, state):
    global rgblist
    if state and rgblist == off:
        rgblist = candle
        keybow.set_led(index, rgblist[0], rgblist[1], rgblist[2])
    elif state and rgblist == candle:
        rgblist = fortyw
        keybow.set_led(index, rgblist[0], rgblist[1], rgblist[2])
    elif state and rgblist == fortyw:
        rgblist = hundredw
        keybow.set_led(index, rgblist[0], rgblist[1], rgblist[2])
    elif state and rgblist == hundredw:
        rgblist = halogen
        keybow.set_led(index, rgblist[0], rgblist[1], rgblist[2])
    elif state and rgblist == halogen:
        rgblist = carbon
        keybow.set_led(index, rgblist[0], rgblist[1], rgblist[2])
    elif state and rgblist == carbon:
        rgblist = off
        keybow.set_led(index, rgblist[0], rgblist[1], rgblist[2])
    return rgblist

#TODO CLEAR ALL WITH MIDDLE BUTTON
@keybow.on(index=1)
def handle_key(index, state):
    if state:
        keybow.set_led(index, brightlist[0], brightlist[1], brightlist[2])
    else:
        keybow.set_led(index, 0, 0, 0)

@keybow.on(index=2)
def handle_key(index, state):
    global brightlist
    if state and brightlist == off:
        brightlist = quarter
        keybow.set_led(index, brightlist[0], brightlist[1], brightlist[2])
    elif state and brightlist == quarter:
        brightlist = half
        keybow.set_led(index, brightlist[0], brightlist[1], brightlist[2])
    elif state and brightlist == half:
        brightlist = threequarter
        keybow.set_led(index, brightlist[0], brightlist[1], brightlist[2])
    elif state and brightlist == threequarter:
        brightlist = full
        keybow.set_led(index, brightlist[0], brightlist[1], brightlist[2])
    elif state and brightlist == full:
        brightlist = off
        keybow.set_led(index, brightlist[0], brightlist[1], brightlist[2])
    return brightlist

# main loop -- TODO function that takes current state + dictionary and returns next state
while True:
    mote.clear()
    mote2.clear()
    mote.set_all(rgblist[0], rgblist[1], rgblist[2])
    mote2.set_all(brightlist[0], brightlist[1], brightlist[2])
    mote.show()
    mote2.show()
    keybow.show()
    time.sleep(0.2)
