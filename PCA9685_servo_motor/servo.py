# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.9
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_lmin= 150  # Min pulse length out of 4096
servo_lmax = 600

servo_rmin=600
servo_rmax=150

servo_legd = 280
servo_legu = 630

  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse) #right
    pwm.set_pwm(channel, 1, pulse) #right

    pwm.set_pwm(channel, 2, pulse) #left
    pwm.set_pwm(channel, 3, pulse) #left

    pwm.set_pwm(channel, 4, pulse) #leg
    pwm.set_pwm(channel, 5, pulse) #leg

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
print('Moving servo on channel 0, press Ctrl-C to quit...')
print(" ")
while True:
    var = input("Enter L/R/LB/RB/LEGU/LEGD: ")
    if var == 'R' or var == 'r' :
        print("Right")
        pwm.set_pwm(0, 0, servo_rmax)
        pwm.set_pwm(1, 0, servo_rmax)
        time.sleep(1)
    elif var == 'L' or var == 'l':
        print("Left")
        pwm.set_pwm(2, 0, servo_lmax)
        pwm.set_pwm(3, 0, servo_lmax)
        time.sleep(1)

    elif var == 'RB' or var == 'rb':
        print("Right Back")
        pwm.set_pwm(0, 0, servo_rmin)
        pwm.set_pwm(1, 0, servo_rmin)
        time.sleep(1)
    elif var == 'lB' or var == 'lb':
        print("Left Back")
        pwm.set_pwm(2, 0, servo_lmin)
        pwm.set_pwm(3, 0, servo_lmin)
        time.sleep(1)

    elif var == 'LEGU' or var == 'legu':
        print("LEG Up")
        pwm.set_pwm(4, 0, servo_legu)
        pwm.set_pwm(5, 0, servo_legu)
        time.sleep(1)
    elif var == 'LEGD' or var == 'legd':
        print("LEG down")
        pwm.set_pwm(4, 0, servo_legd)
        pwm.set_pwm(5, 0, servo_legd)
        time.sleep(1)
    else:
        print("error")

