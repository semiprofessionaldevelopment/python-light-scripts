#!/usr/bin/env python
# see https://github.com/pimoroni/mote for installation instructions 

import time

from mote import Mote
from gpiozero import Button
from signal import pause

button_map = {5: "A",
              6: "B",
              16: "X",
              24: "Y"}

button_a = Button(5)
button_b = Button(6)
button_x = Button(16)
button_y = Button(24)

# On user input, this program mutates red, green, and blue values in rgblist an>

# Default RGB definitions (ie. off)
R = 0
G = 0
B = 0
rgblist = [R, G, B]
brightlist = [R, G, B]

#mote definitions
mote = Mote(port_name='/dev/ttyACM0')
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)
mote.clear()

## add mote2
mote2 = Mote(port_name='/dev/ttyACM1')
mote2.configure_channel(1, 16, False)
mote2.configure_channel(2, 16, False)
mote2.configure_channel(3, 16, False)
mote2.configure_channel(4, 16, False)
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
    # Button A cycles thorugh light warmth
    if button_a.is_pressed and rgblist == off:
        rgblist = candle
    elif button_a.is_pressed and rgblist == candle:
        rgblist = fortyw
    elif button_a.is_pressed and rgblist == fortyw:
        rgblist = hundredw
    elif button_a.is_pressed and rgblist == hundredw:
        rgblist = halogen
    elif button_a.is_pressed and rgblist == halogen:
        rgblist = carbon
    elif button_a.is_pressed and rgblist == carbon:
        rgblist = off

    # Button B cycles through brightness
    elif button_b.is_pressed and brightlist == off:
        brightlist = quarter
    elif button_b.is_pressed and brightlist == quarter:
        brightlist = half
    elif button_b.is_pressed and brightlist == half:
        brightlist = threequarter
    elif button_b.is_pressed and brightlist == threequarter:
        brightlist = full
    elif button_b.is_pressed and brightlist == full:
        brightlist = off

    # Button X turns all lists to off
    if button_x.is_pressed:
        rgblist = off
        brightlist = off

    mote.clear()
    mote2.clear()
    mote.set_all(rgblist[0], rgblist[1], rgblist[2])
    mote2.set_all(brightlist[0], brightlist[1], brightlist[2])
    mote.show()
    mote2.show()
    time.sleep(0.2)
