# log.py
# Registro de acciones en log.txt

LOG_FILE = "log.txt"
op_counter = 1  # contador global de operaciones


def registrar_accion(mensaje):
    global op_counter
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[Op #{op_counter}] {mensaje}\n")
    op_counter += 1
