# python-light-scripts

This repository is a collection of python scripts written for LED light projects. The purpose of this project is to learn about python, repositories and git, and github in general. A Raspberry Pi (4, 3A+, B+ or Zero W) is recommended but not requred. Scripts here are listed with their component and general purpose (such as `unicornhathd-desklight.py`). Please feel free to contribute scripts to this repository for a component or use.

All scripts are single file that runs in the terminal and takes a user interface loop that allows for changes or turns off on exit.

## Supported Components:
- [Unicorn Hat HD](https://github.com/pimoroni/unicorn-hat-hd) by [Pimoroni](https://shop.pimoroni.com/products/unicorn-hat-hd)
- [Mote Kit](https://github.com/pimoroni/mote) by [Pimoroni](https://shop.pimoroni.com/products/mote)

## Use cases:
- ***Desk light***: a light program that functions as a desk lamp with various warmth options (such as candle, 50W bulb, to carbon arc as defined by Kelvin temperature) for comfort and tasks.

---

# Project Status

### Target State:
A plug-and-play light system controlled by one or more buttons that adjust attributes of the light such as the temperature and/or brightness.

### Current State:
Each component has a single file for its use-case, with a UI loops that accepts commands 1~5 in the terminal to adjust temperature.

### Obstacles:
Knowledge of Python and user interfaces.
Knowledge of Git & Repo managmenet. (ie. Do I have the right abstraction of information? Should there be a branch for each component and/or use case? Is a git branch intended to be the feature or the suite?)

### Next Step:
- [ ] Expand use cases to include fun colours and applications such as video flash, key light, or colour splash wall options.
- [ ] Add [Squid Combo Pack](https://gpiozero.readthedocs.io/en/stable/) by [Monk Makes](http://www.monkmakes.com/squid_combo.html) using GPIOZERO.
- [ ] For unicornhathd add option to adjust brightness.

---

## Resources and References

From [RGB to Kelvin Temperature](https://andi-siess.de/rgb-to-color-temperature/):
```
kelvin_table = {
    1000: (255, 56, 0),
    1100: (255, 71, 0),
    1200: (255, 83, 0),
    1300: (255, 93, 0),
    1400: (255, 101, 0),
    1500: (255, 109, 0),
    1600: (255, 115, 0),
    1700: (255, 121, 0),
    1800: (255, 126, 0),
    1900: (255, 131, 0),
    2000: (255, 138, 18),
    2100: (255, 142, 33),
    2200: (255, 147, 44),
    2300: (255, 152, 54),
    2400: (255, 157, 63),
    2500: (255, 161, 72),
    2600: (255, 165, 79),
    2700: (255, 169, 87),
    2800: (255, 173, 94),
    2900: (255, 177, 101),
    3000: (255, 180, 107),
    3100: (255, 184, 114),
    3200: (255, 187, 120),
    3300: (255, 190, 126),
    3400: (255, 193, 132),
    3500: (255, 196, 137),
    3600: (255, 199, 143),
    3700: (255, 201, 148),
    3800: (255, 204, 153),
    3900: (255, 206, 159),
    4000: (255, 209, 163),
    4100: (255, 211, 168),
    4200: (255, 213, 173),
    4300: (255, 215, 177),
    4400: (255, 217, 182),
    4500: (255, 219, 186),
    4600: (255, 221, 190),
    4700: (255, 223, 194),
    4800: (255, 225, 198),
    4900: (255, 227, 202),
    5000: (255, 228, 206),
    5100: (255, 230, 210),
    5200: (255, 232, 213),
    5300: (255, 233, 217),
    5400: (255, 235, 220),
    5500: (255, 236, 224),
    5600: (255, 238, 227),
    5700: (255, 239, 230),
    5800: (255, 240, 233),
    5900: (255, 242, 236),
    6000: (255, 243, 239),
    6100: (255, 244, 242),
    6200: (255, 245, 245),
    6300: (255, 246, 247),
    6400: (255, 248, 251),
    6500: (255, 249, 253),
    6600: (254, 249, 255),
    6700: (252, 247, 255),
    6800: (249, 246, 255),
    6900: (247, 245, 255),
    7000: (245, 243, 255),
    7100: (243, 242, 255),
    7200: (240, 241, 255),
    7300: (239, 240, 255),
    7400: (237, 239, 255),
    7500: (235, 238, 255),
    7600: (233, 237, 255),
    7700: (231, 236, 255),
    7800: (230, 235, 255),
    7900: (228, 234, 255),
    8000: (227, 233, 255),
    8100: (225, 232, 255),
    8200: (224, 231, 255),
    8300: (222, 230, 255),
    8400: (221, 230, 255),
    8500: (220, 229, 255),
    8600: (218, 229, 255),
    8700: (217, 227, 255),
    8800: (216, 227, 255),
    8900: (215, 226, 255),
    9000: (214, 225, 255),
    9100: (212, 225, 255),
    9200: (211, 224, 255),
    9300: (210, 223, 255),
    9400: (209, 223, 255),
    9500: (208, 222, 255),
    9600: (207, 221, 255),
    9700: (207, 221, 255),
    9800: (206, 220, 255),
    9900: (205, 220, 255),
    10000: (207, 218, 255),
    10100: (207, 218, 255),
    10200: (206, 217, 255),
    10300: (205, 217, 255),
    10400: (204, 216, 255),
    10500: (204, 216, 255),
    10600: (203, 215, 255),
    10700: (202, 215, 255),
    10800: (202, 214, 255),
    10900: (201, 214, 255),
    11000: (200, 213, 255),
    11100: (200, 213, 255),
    11200: (199, 212, 255),
    11300: (198, 212, 255),
    11400: (198, 212, 255),
    11500: (197, 211, 255),
    11600: (197, 211, 255),
    11700: (197, 210, 255),
    11800: (196, 210, 255),
    11900: (195, 210, 255),
    12000: (195, 209, 255)}
    ```
