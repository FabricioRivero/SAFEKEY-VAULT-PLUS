# ============================================================
# log.py
# Módulo de LOG (auditoría).
# - Registra cada acción importante del sistema en log.txt.
# - Usa un contador simple de operaciones.
# ============================================================

LOG_FILE = "log.txt"
op_counter = 1  # Contador global de operaciones realizadas


def registrar_accion(mensaje):
    """
    Escribe una línea en el archivo de log, con un número de operación.
    Ejemplo:
        [Op #1] Añadida contraseña para 'Gmail'.
    """
    global op_counter
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[Op #{op_counter}] {mensaje}\n")
    op_counter += 1
