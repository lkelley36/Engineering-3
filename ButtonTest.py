import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

btn = DigitalInOut(board.D9)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

btn2 = DigitalInOut(board.D10)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

while True:
    if  btn.value:
        print("BTN is pressed")
        
    if  btn2.value:
        print("BTN2 is pressed")
       

    time.sleep(0.1) # sleep for debounce

   