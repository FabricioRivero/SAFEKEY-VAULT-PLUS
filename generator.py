# generator.py
# Genera contraseñas seguras aleatorias

import random


def generar_password(longitud, usar_mayus, usar_nums, usar_simbolos):
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()-_+=[]{};:,.<>?"

    pool = minusculas
    if usar_mayus:
        pool += mayusculas
    if usar_nums:
        pool += numeros
    if usar_simbolos:
        pool += simbolos

    if not pool:
        pool = minusculas

    res = []
    for _ in range(longitud):
        res.append(random.choice(pool))
    return ''.join(res)
