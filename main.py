# main.py
# Punto de entrada de SAFEKEY VAULT+

import random

from auth import cargar_master, inicializar_master, verificar_master
from storage import cargar_registros
from password_manager import (
    agregar_password,
    mostrar_password,
    editar_password,
    eliminar_password,
)
from search import menu_buscador
from generator import generar_password
from integrity import revisar_integridad_recursiva
from log import registrar_accion


def menu_principal():
    random.seed()

    master_cifrada = cargar_master()
    if not master_cifrada:
        master_cifrada = inicializar_master()

    if not verificar_master(master_cifrada):
        return

    registros = cargar_registros()

    while True:
        print("\n===== SAFEKEY VAULT+ =====")
        print("1) Agregar nueva contraseña")
        print("2) Consultar contraseñas")
        print("3) Editar contraseña")
        print("4) Eliminar contraseña")
        print("5) Buscador inteligente")
        print("6) Generar contraseña segura")
        print("7) Revisar integridad (recursiva)")
        print("8) Salir")

        try:
            op = int(input("Elige opción: "))
        except ValueError:
            print("Opción inválida.")
            continue

        if op == 1:
            agregar_password(registros)
        elif op == 2:
            mostrar_password(registros)
        elif op == 3:
            editar_password(registros)
        elif op == 4:
            eliminar_password(registros)
        elif op == 5:
            menu_buscador(registros)
        elif op == 6:
            try:
                longitud = int(input("Longitud: "))
            except ValueError:
                print("Longitud inválida.")
                continue
            usar_m = input("¿Incluir mayúsculas? (S/N): ").strip().lower() == "s"
            usar_n = input("¿Incluir números? (S/N): ").strip().lower() == "s"
            usar_s = input("¿Incluir símbolos? (S/N): ").strip().lower() == "s"
            pwd = generar_password(longitud, usar_m, usar_n, usar_s)
            print(f"Contraseña generada: {pwd}")
            registrar_accion("Generada contraseña segura.")
        elif op == 7:
            revisar_integridad_recursiva(registros, 0)
            print("Revisión de integridad completada. Revisa log.txt para detalles.")
        elif op == 8:
            print("Saliendo de SAFEKEY VAULT+ ...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu_principal()
