# ============================================================
# generator.py
# Módulo para GENERAR CONTRASEÑAS SEGURAS aleatorias.
# El usuario decide:
# - Longitud
# - Si usa mayúsculas, números y símbolos
# ============================================================

import random


def generar_password(longitud, usar_mayus, usar_nums, usar_simbolos):
    """
    Genera una contraseña aleatoria en base a la longitud indicada
    y a las opciones de tipos de caracteres.
    """
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()-_+=[]{};:,.<>?"

    # Por defecto, siempre hay minúsculas
    pool = minusculas
    if usar_mayus:
        pool += mayusculas
    if usar_nums:
        pool += numeros
    if usar_simbolos:
        pool += simbolos

    # Seguridad: si por algún motivo el pool queda vacío
    if not pool:
        pool = minusculas

    # Armamos la contraseña carácter por carácter
    res = []
    for _ in range(longitud):
        res.append(random.choice(pool))
    return ''.join(res)
