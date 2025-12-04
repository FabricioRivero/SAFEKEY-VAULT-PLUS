# auth.py
# Manejo de la contraseña maestra

import os
from crypto import cifrar_cesar
from log import registrar_accion

CONFIG_FILE = "config.txt"


def cargar_master():
    if not os.path.exists(CONFIG_FILE):
        return ""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


def guardar_master(master_cifrada):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(master_cifrada)


def inicializar_master():
    print("No existe contraseña maestra. Debes crear una.")
    master = input("Nueva contraseña maestra: ")
    cifrada = cifrar_cesar(master, 3)
    guardar_master(cifrada)
    registrar_accion("Creada contraseña maestra inicial.")
    return cifrada


def verificar_master(master_guardada):
    intentos = 0
    while intentos < 3:
        entrada = input("Introduce contraseña maestra: ")
        cifrada = cifrar_cesar(entrada, 3)
        if cifrada == master_guardada:
            print("✔ Acceso concedido\n")
            registrar_accion("Acceso autorizado con master password.")
            return True
        else:
            print("❌ Incorrecta")
            intentos += 1
    print("❌ Demasiados intentos. Sistema bloqueado.")
    registrar_accion("Sistema bloqueado por intentos fallidos.")
    return False
