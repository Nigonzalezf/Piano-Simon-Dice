from machine import Pin, PWM, TouchPad
from neopixel import NeoPixel
import time

Buzzer = PWM(Pin(19))
pixels = NeoPixel(Pin(23), 12) # El 12 es para indicar que se usaran 13 leds de la tira

# capacitiveValue = 500
# threshold = 150

# Configuración teclas negras
Cs = Pin(4, Pin.IN, Pin.PULL_DOWN)
Ds = Pin(5, Pin.IN, Pin.PULL_DOWN)
Fs = Pin(18, Pin.IN, Pin.PULL_DOWN)
Gs = Pin(26, Pin.IN, Pin.PULL_DOWN)
As = Pin(25, Pin.IN, Pin.PULL_DOWN)

# Configuración teclas blancas
C = TouchPad(Pin(13))
D = TouchPad(Pin(12))
E = TouchPad(Pin(14))
F = TouchPad(Pin(27))
G = TouchPad(Pin(33))
A = TouchPad(Pin(32))
B = TouchPad(Pin(15))
D2 = TouchPad(Pin(2))

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


while True:

    # Do Sostenido
    if Cs.value() == 1:
        print("Do Sostenido")

        # Prender led
        pixels[1] = color['DoS']
        pixels.write()
        time.sleep(0.5)
        pixels[1] = color['Apagar']
        pixels.write()

        # Tocar nota
        Buzzer.freq(int(nota['DoS']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # Re Sostenido
    if Ds.value() == 1:
        print("Re Sostenido")

        pixels[3] = color['ReS']
        pixels.write()
        time.sleep(0.5)
        pixels[3] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['ReS']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)
    
    # Fa Sostenido
    if Fs.value() == 1:
        print("Fa Sostenido")
        
        pixels[6] = color['FaS']
        pixels.write()
        time.sleep(0.5)
        pixels[6] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['FaS']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)
    
    # Sol Sostenido
    if Gs.value() == 1:
        print("Sol Sostenido")
        
        pixels[8] = color['SolS']
        pixels.write()
        time.sleep(0.5)
        pixels[8] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['SolS']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # La Sostenido
    if As.value() == 1:
        print("La Sostenido")
        
        pixels[10] = color['LaS']
        pixels.write()
        time.sleep(0.5)
        pixels[10] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['LaS']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)
"""
    # Do
    if C.read() < threshold:
        print("Do")
        
        pixels[0] = color['Do']
        pixels.write()
        time.sleep(0.5)
        pixels[0] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['Do']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # Re
    if D.read() < threshold:
        print("Re")
        
        pixels[2] = color['Re']
        pixels.write()
        time.sleep(0.5)
        pixels[2] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['Re']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # Mi
    if E.read() < threshold:
        print("Mi")
        
        pixels[4] = color['Mi']
        pixels.write()
        time.sleep(0.5)
        pixels[4] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['Mi']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # Fa
    if F.read() < threshold:
        print("Fa")
        
        pixels[5] = color['Fa']
        pixels.write()
        time.sleep(0.5)
        pixels[5] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['Fa']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # Sol
    if G.read() < threshold:
        print("Sol")
        
        pixels[7] = color['Sol']
        pixels.write()
        time.sleep(0.5)
        pixels[7] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['Sol']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # La
    if A.read() < threshold:
        print("La")
        
        pixels[9] = color['La']
        pixels.write()
        time.sleep(0.5)
        pixels[9] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['La']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # Si
    if B.read() < threshold:
        print("Si")
        
        pixels[11] = color['Si']
        pixels.write()
        time.sleep(0.5)
        pixels[11] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['Si']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)

    # Do 2
    if D2.read() < threshold:
        print("Do 2")
        
        pixels[12] = color['Do2']
        pixels.write()
        time.sleep(0.5)
        pixels[12] = color['Apagar']
        pixels.write()

        Buzzer.freq(int(nota['Do2']))
        Buzzer.duty(230)
        time.sleep(0.5)
        Buzzer.duty(0)
        time.sleep(0.1)
"""
