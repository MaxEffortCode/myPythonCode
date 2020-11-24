#!/usr/bin/python
import pyautogui
import RPi.GPIO as GPIO
import time
import os

global red, green, blue

def getPixVal():
    im1 = pyautogui.screenshot()
    #pix1 = im1.getpixel((384,216))
    #pix2 = im1.getpixel((384*2,216*2))
    pix3 = im1.getpixel((384*3,216*3))
    #pix4 = im1.getpixel((384*4,216*4))
    #pix5 = im1.getpixel(((384*5)-1,(216*5)-1))
    print(pix3)
    return pix3




GPIO.setmode(GPIO.BCM)

# GPIO | Relay
#--------------
# 26     01
# 19     02
# 13     03
# 06     04
# 12     05
# 16     06
# 20     07
# 21     08

# initiate list with pin gpio pin numbers

gpioListAll = [26, 19, 13, 6, 12, 16, 20, 21]
gpioList = [26, 19, 13, 6]
#26 is 12v+, 19 is Blue, 13 is Green, 6 is Red

#sets up the pins for out instructions
def GPIO_SetOut():
    for i in gpioList:
        GPIO.setup(i, GPIO.OUT)




def turnRed():
    GPIO.output(19, GPIO.HIGH)  #GPIO.HIGH CLOSES THE SWITCH

def offRed():
    GPIO.output(19, GPIO.LOW)


def turnGreen():
    GPIO.output(13, GPIO.HIGH)  #GPIO.HIGH CLOSES THE SWITCH

def offGreen():
    GPIO.output(13, GPIO.LOW)
            

def turnBlue():
    GPIO.output(6, GPIO.HIGH)  #GPIO.HIGH CLOSES THE SWITCH

def offBlue():
    GPIO.output(6, GPIO.LOW)




if __name__ == '__main__': 
    rgb = getPixVal()
    if rgb[0] > 50:
        turnRed()
    else:
        offRed()

    if rgb[1] > 50:
        turnGreen()
    else:
        offGreen()

    if rgb[2] > 50:
        turnBlue()
    else:
        offBlue()
