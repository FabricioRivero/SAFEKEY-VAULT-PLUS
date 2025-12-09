# ============================================================
# auth.py
# Módulo responsable de la CONTRASEÑA MAESTRA del sistema.
# - Carga y guarda la master en un archivo.
# - Cifra la master con el método César.
# - Controla los intentos de acceso (máximo 3).
# ============================================================

import os
from crypto import cifrar_cesar
from log import registrar_accion

# Nombre del archivo donde se guarda la contraseña maestra cifrada
CONFIG_FILE = "config.txt"


def cargar_master():
    """
    Lee la contraseña maestra cifrada desde el archivo CONFIG_FILE.
    Si el archivo no existe, devuelve cadena vacía.
    """
    if not os.path.exists(CONFIG_FILE):
        return ""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


def guardar_master(master_cifrada):
    """
    Guarda la contraseña maestra cifrada en CONFIG_FILE.
    """
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(master_cifrada)


def inicializar_master():
    """
    Se ejecuta la PRIMERA VEZ que no existe master guardada.
    - Pide al usuario que cree una nueva contraseña maestra.
    - La cifra con el método César.
    - La guarda en el archivo.
    """
    print("No existe contraseña maestra. Debes crear una.")
    master = input("Nueva contraseña maestra: ")
    cifrada = cifrar_cesar(master, 3)
    guardar_master(cifrada)
    registrar_accion("Creada contraseña maestra inicial.")
    return cifrada


def verificar_master(master_guardada):
    """
    Verifica que la contraseña ingresada por el usuario coincida
    con la que está guardada (comparando la versión cifrada).
    Permite un máximo de 3 intentos.
    """
    intentos = 0
    while intentos < 3:
        entrada = input("Introduce contraseña maestra: ")
        cifrada = cifrar_cesar(entrada, 3)

        # Compara la contraseña ingresada (cifrada) con la guardada
        if cifrada == master_guardada:
            print("✔ Acceso concedido\n")
            registrar_accion("Acceso autorizado con master password.")
            return True
        else:
            print(" Incorrecta")
            intentos += 1

    # Si llega aquí es porque falló 3 veces
    print(" Demasiados intentos. Sistema bloqueado.")
    registrar_accion("Sistema bloqueado por intentos fallidos.")
    return False
