from machine import Pin
import neopixel
from time import sleep

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b, 128)
    np.write()

n = 12
p = 15

np = neopixel.NeoPixel(Pin(p), n)
while True:
    print("test")
    set_color(255, 0, 0)
    sleep(0.8)
    set_color(0, 0, 0)
    sleep(0.8)


