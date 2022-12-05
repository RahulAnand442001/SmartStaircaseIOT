import time
from neopixel import NeoPixel
from machine import Pin
from random import randint

def top_to_bottom(strip, pixel_count, color):
    """
    Control the top of the stairs.
    :param strip: The ws2812b strip
    :param pixel_count: The number of pixels in the pixels strip
    :param color: The color of the pixels strip
    """
    for i in range(pixel_count):
        strip[i] = color
        strip.write()


def bottom_to_top(strip, pixel_count, color):
    """
    This is a function to control the bottom of the stairs.
    :param strip: The ws2812b strip
    :param pixel_count: The number of pixels in the pixels strip
    :param color: The color of the pixels strip
    """
    for i in range(pixel_count - 1, 0, -1):
        strip[i] = color
        strip.write()


# How many pixels do we have?
PIXEL_COUNT = 300

# How long should we keep the light on?
LIGHT_MINUTES = 0.5

# Which pin controls the light strip?
PIXEL_PIN = Pin(0)

# Which pin controls the motion detector?
DOWN_MOTION_DETECTION_PIN = 1
UP_MOTION_DETECTION_PIN = 2

# Which pin controls the light sensor?
#DARKNESS_DETECTION_PIN = 3

# Define the color we want to use for the light strip
UP_COLORS = (randint(0,255),randint(0,255),randint(0,255))
DOWN_COLORS = (randint(0,255),randint(0,255),randint(0,255))

# Define how we want to turn off the light strip
OFF = (0, 0, 0)

# How long should we stay on after detecting motion?
SHINE_TIME = 60 * LIGHT_MINUTES

pixels = NeoPixel(PIXEL_PIN, PIXEL_COUNT)
down = Pin(DOWN_MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)
up = Pin(UP_MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)
#dark = Pin(DARKNESS_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)

pixels.fill(OFF)
pixels.write()

while True:
    if down.value():
        top_to_bottom(pixels, PIXEL_COUNT, UP_COLORS )
        time.sleep(SHINE_TIME)
        top_to_bottom(pixels, PIXEL_COUNT, OFF)
    elif up.value():
        bottom_to_top(pixels, PIXEL_COUNT, DOWN_COLORS)
        time.sleep(SHINE_TIME)
        bottom_to_top(pixels, PIXEL_COUNT, OFF)
