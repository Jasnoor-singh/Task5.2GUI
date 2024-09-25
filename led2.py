import RPi.GPIO as GPIO
from tkinter import Tk, Scale, HORIZONTAL

GPIO.setmode(GPIO.BCM)

RED_LED_PIN = 18
GREEN_LED_PIN = 23
BLUE_LED_PIN = 24

GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

red_pwm = GPIO.PWM(RED_LED_PIN, 1000)
green_pwm = GPIO.PWM(GREEN_LED_PIN, 1000)
blue_pwm = GPIO.PWM(BLUE_LED_PIN, 1000)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

def update_red_led(value):
    red_pwm.ChangeDutyCycle(int(value))

def update_green_led(value):
    green_pwm.ChangeDutyCycle(int(value))

def update_blue_led(value):
    blue_pwm.ChangeDutyCycle(int(value))

root = Tk()
root.title("LED Brightness Control")

red_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Red LED", command=update_red_led)
red_slider.pack()

green_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Green LED", command=update_green_led)
green_slider.pack()

blue_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Blue LED", command=update_blue_led)
blue_slider.pack()

root.mainloop()

red_pwm.stop()
green_pwm.stop()
blue_pwm.stop()
GPIO.cleanup()
