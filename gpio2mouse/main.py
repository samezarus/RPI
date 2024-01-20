# https://www.waveshare.net/wiki/GamePi43

# RPI 4 disable local pip: sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED


import os
os.environ['DISPLAY'] = ':0'
#os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'

# pip install RPi.GPIO
# sudo apt-get install python-rpi.gpio python3-rpi.gpio
import RPi.GPIO as GPIO

# pip install pyautogui
# sudo apt install scrot python3-tk python3-dev
# For RPI 4 pyautogui work in "https://downloads.raspberrypi.com/raspbian_full/images/raspbian_full-2019-07-12/2019-07-10-raspbian-buster-full.zip"
import pyautogui, sys

# pip install python-uinput
#sudo apt install libudev1
#import uinput


pyautogui.FAILSAFE = False

"""
https://toptechboy.com/understanding-raspberry-pi-4-gpio-pinouts/pinout-corrected-2/

GCLK:
    4

I2C:
    2 - SDA1
    3 - SCL1

SPI:
    10 - MOSI
    9  - MISO
    11 - SCLK
    8  - SEO_N
    7  - SE1_N

UART:
    14 - TX
    15 - RX

"""

CR_UP = 4  # ~
CR_RIGHT=22
CR_DOWN=17
CR_LEFT=27

HK=2
SELECT=9  # ~
START=10  # ~

Y=18
X=15  # ~

B=24
A=25

BCK_LEFT=14  # ~
BCK_RIGHT=23

bcm_pins = [CR_UP, CR_RIGHT, CR_DOWN, CR_LEFT, A, B, HK]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in bcm_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

offset_min = 5
offset_max = 15
offset = offset_min

KEY_A_FLAG = False
KEY_B_FLAG = False
KEY_HK_FLAG = False

while True:
    x, y = pyautogui.position()

    for pin in bcm_pins:
        

        if GPIO.input(pin) == 0:

            if pin == HK:
                KEY_HK_FLAG = True
                
                if offset == offset_min:
                    offset = offset_max
                else:
                    offset = offset_min

            if pin == A:
                pyautogui.click()

            if pin == B:
                pyautogui.click(button='right')

            if pin == CR_UP:
                pyautogui.moveTo(None, y-offset)

            if pin == CR_RIGHT:
                pyautogui.moveTo(x+offset, None)

            if pin == CR_DOWN:
                pyautogui.moveTo(None, y+offset)

            if pin == CR_LEFT:
                pyautogui.moveTo(x-offset, None)

GPIO.cleanup()


#pyautogui.FAILSAFE = False

#x, y = pyautogui.position()
#positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#print(positionStr, end='')
#print('\b' * len(positionStr), end='', flush=True)
