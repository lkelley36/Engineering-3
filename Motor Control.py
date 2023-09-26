import time
import board
import pwmio
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

motor = pwmio.PWMOut(board.D9, frequency=50)



pot = AnalogIn(board.A1)



while True:
    print(pot.value)
    time.sleep(0.1)
    motor.duty_cycle=pot.value