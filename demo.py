import virtualhat
import time

virtualhat.setup()

virtualhat.led_on()
time.sleep(5)
virtualhat.led_off()

light = virtualhat.read_light_level()
print("Current light level: " + str(light))

