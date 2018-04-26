import os
import unicornhathd
import time
from math import cos, sin, radians

def calc_point(r, theta, shift):
    x = round(r * cos(radians(theta))) + shift 
    y = round(r * sin(radians(theta))) + shift

    return x, y

if __name__ == "__main__":
    msg = os.getenv('MESSAGE', None)
    print('Message: ', msg)
    unicornhathd.off()
    unicornhathd.brightness(0.5)

    r = 6
    theta = 0
    while True:
        if theta % 360 == 0:
            theta = 0
        
        for unuse in range(15):
            theta += 5
            x, y = calc_point(r, theta, 8)
            i, j = calc_point(r, theta, 7)
            unicornhathd.set_pixel(x, y, 0, 250, 100)
            unicornhathd.set_pixel(i, j, 0, 150, 250)

        unicornhathd.show()
        time.sleep(0.08)
        unicornhathd.off()
