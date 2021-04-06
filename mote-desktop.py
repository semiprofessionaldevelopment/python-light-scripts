#!/usr/bin/env python
# see https://github.com/pimoroni/mote for installation instructions 

import time

from mote import Mote

# On user input, this program mutates red, gree, and blue values in rgblist and sends them to the buffer (ie. outputs the light colours to the mote LED sticks). The light remains on until another selection is made of the program ends.

# Default RGB definitions (ie. off)
R = 0
G = 0
B = 0
rgblist = [R, G, B]

#mote definitions
mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)
mote.clear()

# Light mode name and RGB code for each (2000, 2700, 3000, 3700, 5000 Kelvin)
candle = [255, 138, 18]
fortyw = [255, 169, 87]
hundredw = [255, 180, 107]
halogen = [255, 201, 148]
carbon = [255, 228, 206]

# print options to select
print("""
Enter $ for light.local mode:
1) Candle light
2) 40W Tungsten bulb
3) 100W Tungsten bulb
4) Halogen bulb
5) Carbon Arc bulb

Press CTRL+C to exit and turn off.
""")

# main loop
try:
    while True:
        # present choice options to user
        choice = input()
        choice = int(choice)
        if choice == 1:
            rgblist = candle
        elif choice == 2:
            rgblist = fortyw
        elif choice == 3:
            rgblist = hundredw
        elif choice == 4:
            rgblist = halogen
        elif choice == 5:
            rgblist = carbon
        mote.clear()
        mote.set_all(rgblist[0], rgblist[1], rgblist[2])
        mote.show()
        time.sleep(1.0 / 60)

except KeyboardInterrupt:
    mote.set_all(0, 0, 0)
    mote.show()
    mote.clear()
