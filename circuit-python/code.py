import time
import board
import neopixel
import displayio
import adafruit_lsm303_accel
import adafruit_lis2mdl
import adafruit_ssd1306
import adafruit_lps2x
import adafruit_sht4x
import adafruit_display_text
import terminalio
import busio
import builtins
from digitalio import DigitalInOut


pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.01)
i2c = board.STEMMA_I2C()
sensor = adafruit_lsm303_accel.LSM303_Accel(i2c)
mag = adafruit_lis2mdl.LIS2MDL(i2c)
lps = adafruit_lps2x.LPS22(i2c)
sht = adafruit_sht4x.SHT4x(i2c)

displayio.release_displays()

# Create the SSD1306 OLED class.
display_width = 128
display_height = 32
display = adafruit_ssd1306.SSD1306_I2C(display_width, display_height, i2c)
# You can change the I2C address with an addr parameter:
# display = adafruit_ssd1306.SSD1306_I2C(display_width, display_height, i2c, addr=0x31)

# fills display with black pixels clearing it
display.fill(0)
display.show()

while True:
#    print("  Running...")
#    pixels.fill((0, 255, 255))    display.fill(0)
#    display.t
#    display.show()
#    time.sleep(0.5)
    accel_x, accel_y, accel_z = sensor.acceleration
    mag_x, mag_y, mag_z = mag.magnetic
    str_acc_x = builtins.str("%.1f" % accel_x)
    str_acc_y = builtins.str("%.1f" % accel_y)
    str_acc_z = builtins.str("%.1f" % accel_z)
    str_mag_x = builtins.str("%.1f" % mag_x)
    str_mag_y = builtins.str("%.1f" % mag_y)
    str_mag_z = builtins.str("%.1f" % mag_z)
    temperature = builtins.str("%.1f C" % lps.temperature)
    humidity = builtins.str("%.1f" % sht.relative_humidity)
    pressure  = builtins.str("%.1f" % lps.pressure)
    display.fill(0)
    display.text("ACC", 5, 0, 1)
    display.text(str_acc_x, 0, 8, 1)
    display.text(str_acc_y, 0, 16, 1)
    display.text(str_acc_z, 0, 24, 1)
    display.text("MAG", 40, 0, 1)
    display.text(str_mag_x, 35, 8, 1)
    display.text(str_mag_y, 35, 16, 1)
    display.text(str_mag_z, 35, 24, 1)
    display.text("ENV", 100, 0, 1)
    display.text(temperature, 90, 16, 1)
    display.text(humidity, 90, 24, 1)
    display.text(pressure, 90, 8, 1)
    display.show()
#    print("Running...")
#    time.sleep(0.5)
