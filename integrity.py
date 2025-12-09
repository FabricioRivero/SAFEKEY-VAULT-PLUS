# ============================================================
# integrity.py
# Módulo para revisar la INTEGRIDAD de los registros.
# - Usa una función RECURSIVA para recorrer todos los registros.
# - Detecta campos vacíos y métodos de cifrado inválidos.
# - Registra los problemas en el log.
# ============================================================

from log import registrar_accion


def revisar_integridad_recursiva(registros, index=0):
    """
    Recorre la lista de registros de forma recursiva.
    Para cada registro:
    - Verifica que haya servicio, usuario y contraseña.
    - Verifica que el método de cifrado sea 'CESAR' o 'REC'.
    Registra cualquier problema detectado.
    """
    # Caso base: ya se revisaron todos los registros
    if index >= len(registros):
        return

    r = registros[index]
    problemas = []

    # 1) Validar campos obligatorios
    if not r["servicio"] or not r["usuario"] or not r["contraseña"]:
        problemas.append("registro incompleto (campos vacíos)")

    # 2) Validar método de cifrado
    if r["metodo"] not in ("CESAR", "REC"):
        problemas.append("método de cifrado no reconocido")

    # Si se encontraron problemas, se registran en el log
    if problemas:
        msg = f"Integridad: problema en índice {index}: " + ", ".join(problemas)
        registrar_accion(msg)

    # Llamada recursiva al siguiente índice
    revisar_integridad_recursiva(registros, index + 1)
