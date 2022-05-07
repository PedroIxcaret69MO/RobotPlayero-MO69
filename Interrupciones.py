from machine import Pin
from utime import sleep_ms

led = Pin(25,Pin.OUT)
left_button = Pin(6, Pin.IN, Pin.PULL_DOWN)
right_button = Pin(7, Pin.IN, Pin.PULL_DOWN)
pressed = False
pressed_button = None

def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        global pressed_button
        pressed_button = pin
    
    if pressed_button is left_button:
        print("LEFT")

    elif pressed_button is right_button:
        print("RIGHT")
    
    pressed = False
    pressed_button = None

left_button.irq(trigger = Pin.IRQ_RISING, handler = button_handler)
right_button.irq(trigger = Pin.IRQ_RISING, handler = button_handler)

while True:
    led.value(1)
    sleep_ms(1000)
    led.value(0)
    sleep_ms(1000)
