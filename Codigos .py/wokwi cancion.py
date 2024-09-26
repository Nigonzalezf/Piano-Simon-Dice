from machine import Pin, PWM
from neopixel import NeoPixel
import time

Buzzer = PWM(Pin(19))
pixels = NeoPixel(Pin(23), 12) # El 12 es para indicar que se usaran 13 leds de la tira

# Frecuencias
nota = {
  'Do': 261.63,
  'DoS': 277.18,
  'Re': 293.66,
  'ReS': 311.13,
  'Mi': 329.63,
  'Fa': 349.23,
  'FaS': 369.99,
  'Sol': 391.99,
  'SolS': 415.30,
  'La': 440.00,
  'LaS': 466.16,
  'Si': 493.88,
  'Do2': 523.25
}

# Codigos RGB
color = {
  'Do': (233, 30, 99),
  'DoS': (255, 30, 0),
  'Re': (255, 110, 34),
  'ReS': (255, 152, 0),
  'Mi': (255, 250, 59),
  'Fa': (205, 255, 57),
  'FaS': (76, 175, 80),
  'Sol': (0, 150, 136),
  'SolS': (0, 188, 212),
  'La': (33, 150, 243),
  'LaS': (0, 17, 255),
  'Si': (121, 0, 255),
  'Do2': (156, 39, 176),
  'Apagar':(0,0,0)
}

# Pixel de la tira led
pixel = {
  'Do': 0,
  'DoS': 1,
  'Re': 2,
  'ReS': 3,
  'Mi': 4,
  'Fa': 5,
  'FaS': 6,
  'Sol': 7,
  'SolS': 8,
  'La': 9,
  'LaS': 10,
  'Si': 11,
  'Do2': 12
}

def cancion1():
    Twinkle = [
        "Do", "Do", "Sol", "Sol", "La", "La", "Sol",
        "Fa", "Fa", "Mi", "Mi", "Re", "Re", "Do",
        "Sol", "Sol", "Fa", "Fa", "Mi", "Mi", "Re",
        "Sol", "Sol", "Fa", "Fa", "Mi", "Mi", "Re", 
        "Do", "Do", "Sol", "Sol", "La", "La", "Sol", 
        "Fa", "Fa", "Mi", "Mi", "Re", "Re", "Do"
    ]

    print("Tocando Twinkle: ")

    for i in Twinkle:
        Buzzer.freq(int(nota[i]))
        Buzzer.duty(230)
        pixels[pixel[i]] = color[i]
        pixels.write()
        print(i)

        time.sleep(0.5)
        Buzzer.duty(0)
        pixels[pixel[i]] = color['Apagar']
        pixels.write()
        time.sleep(0.1)
    time.sleep(1)

    for i in range(0, len(Twinkle) + 1, 2):
        print()
        print("Nivel ",i)

        for j in Twinkle[:i]:
            Buzzer.freq(int(nota[j]))
            Buzzer.duty(230)
            pixels[pixel[j]] = color[j]
            pixels.write()
            print(j)

            time.sleep(0.5)
            Buzzer.duty(0)
            pixels[pixel[j]] = color['Apagar']
            pixels.write()
            time.sleep(0.1)
        time.sleep(1)

while True:
    cancion1()

