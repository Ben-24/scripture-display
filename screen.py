from machine import Pin, I2C # type: ignore
from ssd1306 import SSD1306_I2C

class Screen():
    
    def __init__(self):
        i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

        self.oled = SSD1306_I2C(128, 32, i2c)
        
    def clear_screen(self):
        self.oled.fill(0)
        self.oled.show()
        
    def write_text(self, text, x_locaiton, y_location):
        self.oled.text(text, x_locaiton, y_location)
        self.oled.show()