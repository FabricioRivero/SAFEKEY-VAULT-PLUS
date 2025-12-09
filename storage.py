# ============================================================
# storage.py
# Módulo de PERSISTENCIA DE DATOS.
# - Cargar registros desde el archivo data.txt.
# - Guardar registros en el archivo data.txt.
# ============================================================

import os

DATA_FILE = "data.txt"


def cargar_registros():
    """
    Lee el archivo DATA_FILE línea por línea y construye
    una lista de diccionarios con los campos:
    servicio | usuario | contraseña_cifrada | metodo | fecha
    """
    registros = []
    if not os.path.exists(DATA_FILE):
        return registros

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split("|")
            if len(partes) != 5:
                continue

            servicio, usuario, contraseña, metodo, fecha = partes
            registros.append({
                "servicio": servicio,
                "usuario": usuario,
                "contraseña": contraseña,
                "metodo": metodo,
                "fecha": fecha,
            })
    return registros


def guardar_registros(registros):
    """
    Escribe en DATA_FILE todos los registros de la lista,
    cada uno en una línea en formato separado por '|'.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for r in registros:
            f.write(
                f"{r['servicio']}|{r['usuario']}|{r['contraseña']}|{r['metodo']}|{r['fecha']}\n"
            )
