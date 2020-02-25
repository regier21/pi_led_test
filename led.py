import pigpio
import time

pi = pigpio.pi()
pi.set_mode(13, pigpio.OUTPUT)
pi.set_PWM_frequency(13, 1000)


dcs = range(0,256)
dcs = dcs + list(reversed(dcs))

def brighten(delay):
	for dc in dcs:
		pi.set_PWM_dutycycle(13,dc)
		time.sleep(delay)

brighten(0.02)


