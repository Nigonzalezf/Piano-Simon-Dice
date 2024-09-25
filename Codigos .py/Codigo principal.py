from machine import Pin, PWM, TouchPad, SoftI2C
from neopixel import NeoPixel

from i2c_lcd import I2cLcd
from lcd_api import LcdApi

import time

capacitiveValue = 500
threshold = 150

Buzzer = PWM(Pin(19))
Buzzer.duty(0)
pixels = NeoPixel(Pin(23), 12)

# Datos de la LCD
Filas = 2
Columnas = 16
I2C_Direccion = 0x27
SCL = Pin(22)
SDA = Pin(21)
Frecuencia = 10000
i2c = SoftI2C(scl=SCL, sda=SDA, freq=Frecuencia)
lcd = I2cLcd(i2c, I2C_Direccion, Filas, Columnas)

# Configuracion botones del menu
Bok = Pin(16, Pin.IN, Pin.PULL_DOWN)
Bnext = Pin(17, Pin.IN, Pin.PULL_DOWN)

# Configuración teclas negras
Cs = Pin(34, Pin.IN, Pin.PULL_DOWN)
Ds = Pin(35, Pin.IN, Pin.PULL_DOWN)
Fs = Pin(18, Pin.IN, Pin.PULL_DOWN)
Gs = Pin(26, Pin.IN, Pin.PULL_DOWN)
As = Pin(25, Pin.IN, Pin.PULL_DOWN)

C = TouchPad(Pin(13))
D = TouchPad(Pin(12))
E = TouchPad(Pin(14))
F = TouchPad(Pin(27))
G = TouchPad(Pin(33))
A = TouchPad(Pin(32))
B = TouchPad(Pin(15))
D2 = TouchPad(Pin(4))

contador = 0
presionado = False

cancionMenu = (
  "Twinkle Twinkle Little Star   ->",
  "Wheels on       the Bus       ->",
  "Mary had a      Little Lamb   ->",
  "Row row row     your Boat     ->",
  "Jingle Bells                  ->"
)

# Botones
boton = {
  'DoS': Cs,
  'ReS': Ds,
  'FaS': Fs,
  'SolS': Gs,
  'LaS': As,
}

# Sensores
sensor = {
  'Do': C,
  'Re': D,
  'Mi': E,
  'Fa': F,
  'Sol': G,
  'La': A,
  'Si': B,
  'Do2': D2
}

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

cancion = {
    "prueba" : ["DoS", "DoS", "ReS", "ReS", "FaS", "FaS", "SolS", "SolS", "LaS", "LaS"],
    "Twinkle" : ["Do", "Do", "Sol", "Sol", "La", "La", "Sol", "Fa", "Fa", "Mi", "Mi", "Re", "Re", "Do", "Sol", "Sol", "Fa", "Fa", "Mi", "Mi", "Re", "Sol", "Sol", "Fa", "Fa", "Mi", "Mi", "Re", "Do", "Do", "Sol", "Sol", "La", "La", "Sol", "Fa", "Fa", "Mi", "Mi", "Re", "Re", "Do"],
    "Wheels" : ["Do", "Fa", "Fa", "Fa", "Fa", "La", "Do mayor", "La", "Fa", "Sol", "Mi", "Do", "Do mayor", "La", "Fa", "Do", "Fa", "Fa", "Fa", "Fa", "La", "Do mayor", "La", "Fa", "Sol", "Do", "Do", "Fa" ],
    "Mary" : ["Mi", "Re", "Do", "Re", "Mi", "Mi", "Mi", "Re", "Re", "Re", "Mi", "Sol", "Sol", "Mi", "Re", "Do", "Re", "Mi", "Mi", "Mi", "Mi", "Re", "Re", "Mi", "Re", "Do" ],
    "Row" : ["Do", "Do", "Do", "Re", "Mi", "Mi", "Re", "Mi", "Fa", "Sol", "Do mayor", "Do mayor", "Do mayor", "Sol", "Sol", "Sol", "Mi", "Mi", "Mi", "Do", "Do", "Do", "Sol", "Fa", "Mi", "Re", "Do" ]
}

def simon():
    lcd.putstr("Primero escucha \nla cancion")
    time.sleep(2)
    lcd.clear()

    for i in cancion["Twinkle"]:
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

    lcd.putstr("Comienza el \njuego!!")
    time.sleep(2)
    lcd.clear()

    lonSecuencia = len(cancion["Twinkle"])
    objSecuencia = cancion["Twinkle"].copy()
    time.sleep(1)

    nivel = 2  # Iniciamos con las primeras 2 notas

    while nivel <= lonSecuencia:
        print()
        print("Nivel ", nivel)

        # Mostrar la secuencia hasta el nivel actual
        for j in objSecuencia[:nivel]:
            Buzzer.freq(int(nota[j]))  # Sonido
            Buzzer.duty(230)

            pixels[pixel[j]] = color[j]  # Led y color
            pixels.write()

            lcd.putstr(j)  # Pantalla
            print(j)

            time.sleep(0.5)

            Buzzer.duty(0)
            pixels[pixel[j]] = color['Apagar']
            pixels.write()
            lcd.clear()
            time.sleep(0.1)
        time.sleep(1)

        # Ahora esperamos la respuesta del usuario
        userSecuencia = []
        while len(userSecuencia) < nivel:  # El usuario debe ingresar la secuencia completa

            for led, sen in sensor.items():
                sen.read() == capacitiveValue
                if capacitiveValue < threshold:
                    Buzzer.freq(int(nota[led]))  # Sonido
                    Buzzer.duty(230)

                    pixels[pixel[led]] = color[led]  # Led y color
                    pixels.write()

                    lcd.putstr(led)  # Pantalla
                    print(led)

                    userSecuencia.append(led)  # Se agrega el nombre del LED a la secuencia del usuario

                    while bot.value():  # Espera a que el usuario suelte el botón
                        time.sleep(0.1)

                    Buzzer.duty(0)
                    pixels[pixel[led]] = color['Apagar']
                    pixels.write()
                    lcd.clear()

                    time.sleep(0.1)

            for led, bot in boton.items():
                if bot.value() == True:  # Si el botón está presionado
                    Buzzer.freq(int(nota[led]))  # Sonido
                    Buzzer.duty(230)

                    pixels[pixel[led]] = color[led]  # Led y color
                    pixels.write()

                    lcd.putstr(led)  # Pantalla
                    print(led)

                    userSecuencia.append(led)  # Se agrega el nombre del LED a la secuencia del usuario

                    while bot.value():  # Espera a que el usuario suelte el botón
                        time.sleep(0.1)

                    Buzzer.duty(0)
                    pixels[pixel[led]] = color['Apagar']
                    pixels.write()
                    lcd.clear()

                    time.sleep(0.1)

        # Comparar la secuencia del usuario con la secuencia actual
        if userSecuencia == objSecuencia[:nivel]:
            lcd.putstr("Secuencia \nCorrecta")
            print("Secuencia correcta")
            time.sleep(3)
            lcd.clear()
            nivel += 2  # Agregar 2 notas a la secuencia
        else:
            lcd.putstr("Secuencia \nIncorrecta")
            print("Secuencia incorrecta")
            time.sleep(3)
            lcd.clear()
            break

    # Mostrar el resultado final
    if nivel > lonSecuencia:
        lcd.putstr("¡Ganaste!")
        print("¡Ganaste!")
        time.sleep(5)
        lcd.clear()
    else:
        lcd.putstr("Has perdido")
        print("Has perdido")
        time.sleep(5)
        lcd.clear()
    
while True:
    # Mensaje de bienvenida
    lcd.putstr("Bienvenido a:\nSimon's Piano")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("Selecciona una\ncancion       ->")
    time.sleep(3)

    if Bnext.value() == 1 and not presionado:
        lcd.clear()
        lcd.putstr(cancionMenu[contador])
        contador = (contador + 1) % len(cancionMenu)
        presionado = True
        time.sleep(0.2)
 
    elif Bnext.value() == 0:
        presionado = False
        
    if Bok.value() == 1 and not presionado:
        time.sleep(2)
        simon()  # Ejecuta la función del juego
        
    elif Bok.value() == 0:
        presionado = False