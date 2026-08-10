import time
import board
import neopixel

pixels = neopixel.NeoPixel(
    board.D18,
    60,
    brightness=0.2,
    auto_write=False
)

pixels.fill((255, 0, 0))
pixels.show()
time.sleep(2)

pixels.fill((0, 255, 0))
pixels.show()
time.sleep(2)

pixels.fill((0, 0, 255))
pixels.show()
time.sleep(2)

pixels.fill((0, 0, 0))
pixels.show()

