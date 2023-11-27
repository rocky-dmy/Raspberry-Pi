import machine
import ssd1306
 
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15), freq=400_000)
print("I2C device: " + str(i2c.scan()[0]))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
 
oled.text("PICO LAB", 0, 0)
oled.hline(0, 10, 128, 1)
oled.text("Hello World!", 0, 26)
oled.hline(0, 48, 128, 1)
oled.text("PICO.NXEZ.COM", 0, 52)
oled.show()
