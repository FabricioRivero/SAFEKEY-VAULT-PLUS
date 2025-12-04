# integrity.py
# Revisión de integridad RECURSIVA de los registros

from log import registrar_accion


def revisar_integridad_recursiva(registros, index=0):
    if index >= len(registros):
        return

    r = registros[index]
    problemas = []

    if not r["servicio"] or not r["usuario"] or not r["contraseña"]:
        problemas.append("registro incompleto (campos vacíos)")

    if r["metodo"] not in ("CESAR", "REC"):
        problemas.append("método de cifrado no reconocido")

    if problemas:
        msg = f"Integridad: problema en índice {index}: " + ", ".join(problemas)
        registrar_accion(msg)

    revisar_integridad_recursiva(registros, index + 1)
