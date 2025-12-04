# storage.py
# Manejo de archivo de datos (contraseñas)

import os

DATA_FILE = "data.txt"


def cargar_registros():
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
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for r in registros:
            f.write(
                f"{r['servicio']}|{r['usuario']}|{r['contraseña']}|{r['metodo']}|{r['fecha']}\n"
            )
