import math


def saludo():
    print("¡¡ Hola Amiga !!")


# saludo()

def saludo_pers(nombre):
    print(f" ¡¡ Hola {nombre} !!")


# nombre="matias"
# saludo_pers(nombre)

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# print(factorial(5))

def calc_iva(monto, iva=21):
    monto_final = monto * (iva / 100)
    return monto_final


# print(calc_iva(2000, 15))
# print(calc_iva(2000))
# print(calc_iva(2000, 21))

def area_circ(diam):
    area = (math.pi * ((diam / 2) ** 2)).__round__(2)
    return area


def vol_circ(diametro, altura):
    volumen = (area_circ(diametro) * altura).__round__(2)
    return volumen


# print(area_circ(25))
# print(vol_circ(25, 90))

def media(list):
    media = sum(list) / len(list)
    return media


# print(media([1, 2, 3, 4, 5]))

def cuadrados(list):
    lista = []
    for i in list:
        lista.append(i ** 2)
    return lista


# print(cuadrados([1, 5, 9, 87, 101]))

def mcd(m, n):
    resto = 0
    while m > 0:
        resto = m
        m = m % n
        resto = n
    return n


def mcm(m, n):
    if n > m:
        mayor = n
    else:
        mayor = m
    while (mayor % n != 0) or (mayor % m != 0):
        mayor += 1
    return mayor


# print(mcd(20, 5))
# print(mcm(20, 11))


def to_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal


def to_string(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return "".join(binary)


# print(to_string(11))
# print(to_decimal("1011"))

def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words


def most_repeated(words):
    max_word = ""
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq


text = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera".lower()


# print(count_words(text))
# print(most_repeated(count_words(text)))

# Se aplica un descuento al valor de la compra
def aply_discount(value, discount):
    value_ultimate = value - (value * discount / 100)
    return value_ultimate


# Se aplica el iva al valor de la compra
def aply_iva(value, iva):
    value_ultimate = value + (value * (iva / 100))
    return value_ultimate


def price_basket(basket, fuction):
    total = 0
    for value, porcentage in basket.items():
        total += fuction(value, porcentage)
    return total


# print(price_basket({1000:20, 500:10, 100:1}, aply_discount))
# print(price_basket({1000:20, 500:10, 100:1}, aply_iva))


