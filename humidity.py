#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()

blue = (0, 0, 255)
white = (255, 255, 255)

while True:
    humidity = sense.humidity
    humidity_value = 64 * humidity / 100
    print(humidity)

    pixels = [blue if i < humidity_value else white for i in range(64)]

    sense.set_pixels(pixels)
