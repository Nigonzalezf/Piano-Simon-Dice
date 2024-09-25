# Prueba pines touch
from machine import Pin, TouchPad
import time

capacitiveValue = 500
threshold = 150
prueaPin = TouchPad(Pin(x))

while True:
	capacitiveValue = pruebaPin.read()
	if capacitiveValue < threshold:
		print("Funciona")
		time.sleep(0.5)
		
# Prueba pines
from machine import Pin
import time

pruebaPin = Pin(x, Pin.IN, Pin.PULL_DOWN)

while True:
	if pruebaPin.value() == 1:
		print("Funciona")
	time.sleep(0.3)