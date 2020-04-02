import random

def setup():
    print("All peripherals and sensors have been set up successfully!")
    return True

def led_on():
    print("The LED is ON")

def led_off():
    print("The LED is OFF")

def read_light_level():
    return random.randint(50,70)

