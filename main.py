import unicornhathd
import time
from math import cos, sin, radians

def calc_point(r, theta, shift):
    x = round(r * cos(radians(theta))) + shift 
    y = round(r * sin(radians(theta))) + shift

    return x, y

if __name__ == "__main__":
    unicornhathd.off()

    r = 6
    theta = 0
    while True:
        if theta % 360 == 0:
            theta = 0
        
        for unuse in range(15):
            theta += 5
            x, y = calc_point(r, theta, 8)
            i, j = calc_point(r, theta, 7)
            unicornhathd.set_pixel(x, y, 100, 250, 0)
            unicornhathd.set_pixel(i, j, 250, 150, 0)

        unicornhathd.show()
        time.sleep(0.08)
        unicornhathd.off()
