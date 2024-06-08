from machine import Pin, I2C # type: ignore
from ssd1306 import SSD1306_I2C

class Screen():
    
    def __init__(self):
        i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

        oled = SSD1306_I2C(128, 32, i2c)

        oled.text('Scrip: 1Cor 13:1-3', 0, 0)
        oled.show()