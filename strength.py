# ============================================================
# strength.py
# Módulo que ANALIZA QUÉ TAN FUERTE es una contraseña.
# - Considera longitud, uso de mayúsculas, minúsculas, números,
#   símbolos y patrones débiles comunes.
# ============================================================


def evaluar_fuerza(contraseña):
    """
    Devuelve una clasificación de la contraseña:
    - DEBIL
    - MEDIA
    - FUERTE
    - MUY FUERTE
    según una puntuación calculada.
    """
    score = 0

    # Longitud mínima
    if len(contraseña) >= 8:
        score += 1
    if len(contraseña) >= 12:
        score += 1

    # Diversidad de caracteres
    if any(c.isupper() for c in contraseña):
        score += 1
    if any(c.islower() for c in contraseña):
        score += 1
    if any(c.isdigit() for c in contraseña):
        score += 1

    simbolos = "!@#$%^&*()-_+=[]{};:,.<>?"
    if any(c in simbolos for c in contraseña):
        score += 1

    # Castigar patrones débiles
    low = contraseña.lower()
    if "123" in low or "password" in low or "abc" in low or "qwerty" in low:
        score -= 2

    # Clasificación final
    if score <= 2:
        return "DEBIL"
    elif score <= 4:
        return "MEDIA"
    elif score <= 6:
        return "FUERTE"
    else:
        return "MUY FUERTE"
