# ============================================================
# password_manager.py
# Módulo de GESTIÓN de contraseñas (CRUD):
# - Listar
# - Agregar
# - Consultar
# - Editar
# - Eliminar
# ============================================================

import time
from crypto import cifrar_cesar, cifrar_recursivo, descifrar_cesar, descifrar_recursivo
from strength import evaluar_fuerza
from storage import guardar_registros
from log import registrar_accion


def fecha_simulada():
    """
    Genera una cadena de fecha y hora actual en formato YYYY-MM-DD HH:MM:SS.
    Se usa como fecha de registro de la contraseña.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")


def listar_servicios(registros):
    """
    Muestra en pantalla todos los servicios almacenados con su índice.
    """
    if not registros:
        print("No hay registros.")
        return
    print("=== LISTA DE SERVICIOS ===")
    for i, r in enumerate(registros):
        print(f"{i}) {r['servicio']} ({r['usuario']})")


def agregar_password(registros):
    """
    Agrega una nueva contraseña al sistema:
    - Pide servicio, usuario y contraseña.
    - Evalúa la fuerza de la contraseña.
    - Permite elegir el método de cifrado.
    - Guarda el registro en memoria y en archivo.
    """
    servicio = input("Servicio: ")
    usuario = input("Usuario/correo: ")
    pwd = input("Contraseña (en texto): ")

    # Analizar fuerza de la contraseña
    fuerza = evaluar_fuerza(pwd)
    print(f"Fuerza estimada: {fuerza}")

    # Elegir método de cifrado
    print("Método de cifrado:")
    print("1) César")
    print("2) Recursivo (inversión + César)")
    while True:
        try:
            op = int(input("Elige opción: "))
            if op in (1, 2):
                break
        except ValueError:
            pass
        print("Opción inválida.")

    if op == 1:
        pwd_cifrada = cifrar_cesar(pwd, 3)
        metodo = "CESAR"
    else:
        pwd_cifrada = cifrar_recursivo(pwd)
        metodo = "REC"

    # Crear registro en formato diccionario
    registro = {
        "servicio": servicio,
        "usuario": usuario,
        "contraseña": pwd_cifrada,
        "metodo": metodo,
        "fecha": fecha_simulada(),
    }

    # Guardar en la lista y en el archivo
    registros.append(registro)
    guardar_registros(registros)
    registrar_accion(f"Añadida contraseña para '{servicio}'.")


def mostrar_password(registros):
    """
    Permite seleccionar un registro y mostrar sus datos.
    Opcionalmente, puede mostrar la contraseña DESCIFRADA.
    """
    if not registros:
        print("No hay registros.")
        return

    listar_servicios(registros)
    try:
        idx = int(input("Elige índice: "))
    except ValueError:
        print("Índice inválido.")
        return

    if idx < 0 or idx >= len(registros):
        print("Índice fuera de rango.")
        return

    r = registros[idx]
    print(f"Servicio: {r['servicio']}")
    print(f"Usuario: {r['usuario']}")
    print(f"Fecha: {r['fecha']}")

    ver = input("¿Mostrar contraseña descifrada? (S/N): ").strip().lower()
    if ver == "s":
        if r["metodo"] == "CESAR":
            original = descifrar_cesar(r["contraseña"], 3)
        elif r["metodo"] == "REC":
            original = descifrar_recursivo(r["contraseña"])
        else:
            original = "(método desconocido)"

        print(f"Contraseña: {original}")
        registrar_accion(f"Consultada contraseña de '{r['servicio']}'.")


def editar_password(registros):
    """
    Permite modificar la contraseña y el método de cifrado
    de un registro ya existente.
    """
    if not registros:
        print("No hay registros.")
        return

    listar_servicios(registros)
    try:
        idx = int(input("Elige índice a editar: "))
    except ValueError:
        print("Índice inválido.")
        return

    if idx < 0 or idx >= len(registros):
        print("Índice fuera de rango.")
        return

    r = registros[idx]
    print(f"Editando servicio: {r['servicio']} (usuario: {r['usuario']})")

    pwd = input("Nueva contraseña (texto): ")
    fuerza = evaluar_fuerza(pwd)
    print(f"Fuerza estimada: {fuerza}")

    print("Método de cifrado:")
    print("1) César")
    print("2) Recursivo")
    while True:
        try:
            op = int(input("Elige opción: "))
            if op in (1, 2):
                break
        except ValueError:
            pass
        print("Opción inválida.")

    if op == 1:
        r["contraseña"] = cifrar_cesar(pwd, 3)
        r["metodo"] = "CESAR"
    else:
        r["contraseña"] = cifrar_recursivo(pwd)
        r["metodo"] = "REC"

    guardar_registros(registros)
    registrar_accion(f"Editada contraseña para '{r['servicio']}'.")


def eliminar_password(registros):
    """
    Elimina un registro (servicio) seleccionado por índice.
    """
    if not registros:
        print("No hay registros.")
        return

    listar_servicios(registros)
    try:
        idx = int(input("Elige índice a eliminar: "))
    except ValueError:
        print("Índice inválido.")
        return

    if idx < 0 or idx >= len(registros):
        print("Índice fuera de rango.")
        return

    servicio = registros[idx]["servicio"]
    registros.pop(idx)
    guardar_registros(registros)
    registrar_accion(f"Eliminada contraseña para '{servicio}'.")
