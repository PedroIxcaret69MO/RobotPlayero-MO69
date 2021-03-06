from DCMOTOR import DCMOTOR
from machine import Pin, PWM
from time import sleep

frequency = 15000

rpwm_d = PWM(Pin(16))
lpwm_d = PWM(Pin(17))
rpwm_i = PWM(Pin(14))
lpwm_i = PWM(Pin(15))

rpwm_d.freq(frequency)
lpwm_d.freq(frequency)
rpwm_i.freq(frequency)
lpwm_i.freq(frequency)

dc_motor = DCMOTOR(rpwm_d, lpwm_d, rpwm_i, lpwm_i, min_duty=0, max_duty=65535)

dc_motor.forward(100)
sleep(2)
dc_motor.stop()
sleep(3)
dc_motor.backwards(100)
sleep(2)
dc_motor.stop()
sleep(3)
dc_motor.left(100)
sleep(2)
dc_motor.stop()
sleep(3)
dc_motor.right(100)
sleep(2)
dc_motor.stop()
