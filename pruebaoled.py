from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
from imagen import (logo)

WIDTH = 128
HEIGHT = 64
i2c = I2C(0,scl = Pin(5), sda = Pin(4))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
buffer = bytearray(logo)
fb = framebuf.FrameBuffer(buffer,WIDTH,HEIGHT,framebuf.MONO_HLSB)
oled.fill(0)
oled.blit(fb,0,0)
oled.text('LISTO', 5, 0)
oled.text('LISTO', 85, 0)
oled.show()
