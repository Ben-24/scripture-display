from machine import Pin, I2C # type: ignore
from ssd1306 import SSD1306_I2C

class Screen():
    
    def __init__(self):
        i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

        self.oled = SSD1306_I2C(128, 32, i2c)
        self.open_row = 0
        
    def clear_screen(self):
        self.oled.fill(0)
        self.open_row = 0
        self.oled.show()
        
    def write_text(self, text, x_locaiton, y_location):
        self.oled.text(text, x_locaiton, y_location)
        self.oled.show()
    
    def write_wrapped_text(self, text):
        if (len(text) > 21):
            text1 = text[0:21]
            text2 = text[21:]
            self.write_text(text1, 0, self.open_row)
            self.open_row += 10
            self.write_text(text2, 0, self.open_row)
            self.open_row += 10
        else:
            self.write_text(text, 0, self.open_row)
            self.open_row += 10