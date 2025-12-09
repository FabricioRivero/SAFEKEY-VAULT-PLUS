# ============================================================
# search.py
# Módulo de BÚSQUEDA DE REGISTROS:
# - Búsqueda exacta por servicio.
# - Búsqueda exacta por usuario.
# - Búsqueda RECURSIVA por coincidencia parcial (en servicio).
# ============================================================

from log import registrar_accion


def buscar_por_servicio(registros, servicio):
    """
    Busca de forma LINEAL un servicio exacto en la lista de registros.
    Devuelve el índice o -1 si no lo encuentra.
    """
    objetivo = servicio.lower()
    for i, r in enumerate(registros):
        if r["servicio"].lower() == objetivo:
            return i
    return -1


def buscar_por_usuario(registros, usuario):
    """
    Busca de forma LINEAL un usuario exacto en la lista de registros.
    Devuelve el índice o -1 si no lo encuentra.
    """
    objetivo = usuario.lower()
    for i, r in enumerate(registros):
        if r["usuario"].lower() == objetivo:
            return i
    return -1


def buscar_coincidencia_recursiva(registros, patron, index=0):
    """
    Búsqueda RECURSIVA:
    Recorre la lista de registros buscando un servicio que
    contenga el patrón indicado (coincidencia parcial).
    Devuelve el índice o -1 si no lo encuentra.
    """
    if index >= len(registros):
        return -1

    p = patron.lower()
    s = registros[index]["servicio"].lower()

    # Si el patrón está contenido en el nombre del servicio
    if p in s:
        return index

    # Llamada recursiva al siguiente índice
    return buscar_coincidencia_recursiva(registros, patron, index + 1)


def menu_buscador(registros):
    """
    Muestra un submenú de búsqueda:
    1) Búsqueda exacta por servicio.
    2) Búsqueda exacta por usuario.
    3) Búsqueda RECURSIVA por coincidencia parcial.
    """
    print("1) Buscar por servicio (exacto)")
    print("2) Buscar por usuario (exacto)")
    print("3) Buscar por coincidencia parcial en servicio (recursivo)")
    try:
        op = int(input("Opción: "))
    except ValueError:
        print("Opción inválida.")
        return

    if op == 1:
        serv = input("Servicio: ")
        idx = buscar_por_servicio(registros, serv)
    elif op == 2:
        usr = input("Usuario: ")
        idx = buscar_por_usuario(registros, usr)
    elif op == 3:
        pat = input("Patrón parcial: ")
        idx = buscar_coincidencia_recursiva(registros, pat, 0)
    else:
        print("Opción inválida.")
        return

    # Mostrar resultado
    if idx == -1:
        print("No encontrado.")
    else:
        r = registros[idx]
        print(f"Encontrado en índice {idx}: {r['servicio']} ({r['usuario']})")
        registrar_accion(f"Búsqueda exitosa. Índice {idx}, servicio '{r['servicio']}'.")
